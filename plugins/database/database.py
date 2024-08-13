from typing import List, Dict
import pymongo
import config
import json

myclient = pymongo.MongoClient(config.db_url)
mydb = myclient[config.db_name]

mycol = mydb['user']


class Database():
    def __init__(self, user_id: int):
        self.user_id = user_id

    async def tambah_databot(self):
        data = {
            "_id": self.user_id,
            "menfess": 0,
            "bot_status": True,
            "ban": {},
            "admin": [],
            "kirimchannel": {
                "photo": True,
                "video": False,
                "voice": False
            }
        }
        await self.tambah_pelanggan(data)

    async def cek_user_didatabase(self):
        found = mycol.find_one({'_id': self.user_id})
        if found:
            return True
        else:
            return False

    async def tambah_pelanggan(self, data):
        mycol.insert_one(data)
    
    async def hapus_pelanggan(self, user_id: int):
        mycol.delete_one({'_id': user_id})
        return

    async def update_menfess(self, coin: int, menfess: int, all_menfess: int):
        user = self.get_data_pelanggan()
        last_coin = user.coin
        last_menfess = user.menfess
        last_all_menfess = user.all_menfess
        mycol.update_one(
            {"coin": f"{last_coin}_{str(user.id)}", "menfess": last_menfess, "all_menfess": last_all_menfess},
            {"$set": {
                "coin": f"{coin}_{str(user.id)}",
                "menfess": (menfess + 1),
                "all_menfess": (all_menfess + 1)}
            }
        )
    async def reset_menfess(self):
        last = {"menfess" : {"$regex": "^[0-9]"}}
        new = { "$set": { "menfess": 0 } }
        x = mycol.update_many({}, new)
        return x.modified_count
        
    async def transfer_coin(self, ditranfer: int, diterima: int, coin_awal_target_full: int, id_target: int):
        coin_awal_user = self.get_data_pelanggan().coin_full
        a = mycol.update_one(
            {"coin": coin_awal_user},
            {"$set": {
                "coin": f"{ditranfer}_{self.user_id}"
            }}
        )
        b = mycol.update_one(
            {"coin": coin_awal_target_full},
            {"$set": {
                "coin": f"{diterima}_{id_target}"
            }}
        )
    async def update_admin(self, id_admin: int, id_bot: int):
        last_data = {
            "admin": self.get_data_bot(id_bot).admin
        }
        data = self.get_data_bot(id_bot).admin
        data.append(id_admin)

        last_status = self.get_data_pelanggan().status_full
        coin_awal = self.get_data_pelanggan().coin
        mycol.update_one(
            {"status": last_status, "coin": f"{coin_awal}_{str(id_admin)}"},
            {"$set": {
                "status": f"admin_{str(id_admin)}",
                "coin": f"{(coin_awal + 1000000)}_{str(id_admin)}"
            }
            })
        mycol.update_one(last_data, {"$set": {"admin": data}})

    async def hapus_admin(self, id_admin: int, id_bot: int):
        last_data = {
            "admin": self.get_data_bot(id_bot).admin
        }
        data = self.get_data_bot(id_bot).admin
        data.remove(id_admin)

        last_status = self.get_data_pelanggan().status_full
        coin_awal = self.get_data_pelanggan().coin
        mycol.update_one(
            {"status": last_status, "coin": f"{coin_awal}_{str(id_admin)}"},
            {"$set": {
                "status": f"member_{str(id_admin)}",
                "coin": f"{(coin_awal - 1000)}_{str(id_admin)}"
            }
            })
        mycol.update_one(last_data, {"$set": {"admin": data}})

    async def banned_user(self, id_banned: int, id_bot: int, alasan: str):
        last_data = {
            "ban": self.get_data_bot(id_bot).ban
        }
        new_data = self.get_data_bot(id_bot).ban
        new_data[str(id_banned)] = str(alasan)
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"banned_{str(id_banned)}"}
             })
        mycol.update_one(last_data, {"$set": {"ban": new_data}})
    
    async def unban_user(self, id_banned: int, id_bot: int):
        last_data = {
            "ban": self.get_data_bot(id_bot).ban
        }
        new_data = self.get_data_bot(id_bot).ban
        del new_data[str(id_banned)]
        last_status = self.get_data_pelanggan().status_full
        mycol.update_one(
            {"status": last_status},
            {"$set": {"status": f"member_{str(id_banned)}"}}
        )
        mycol.update_one(last_data, {"$set": {"ban": new_data}})
    
    async def bot_handler(self, status: str):
        if status == 'on' or status == '<on>':
            bot_status = True
            last_data = {"bot_status": False}
        else:
            bot_status = False
            last_data = {"bot_status": True}

        mycol.update_one(last_data, {"$set": {"bot_status": bot_status}})

    async def photo_handler(self, status: str, id_bot: int):
        data_bot = self.get_data_bot(id_bot).kirimchannel
        last_data = {"kirimchannel": {"photo": data_bot.photo, "video": data_bot.video, "voice": data_bot.voice }}
        if status == '✅':
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": False,
                    "video": data_bot.video,
                    "voice": data_bot.voice
                    }
                }
            }
        else:
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": True,
                    "video": data_bot.video,
                    "voice": data_bot.voice
                    }
                }
            }
        mycol.update_one(last_data, photo_status)

    async def video_handler(self, status: str, id_bot: int):
        data_bot = self.get_data_bot(id_bot).kirimchannel
        last_data = {"kirimchannel": {"photo": data_bot.photo, "video": data_bot.video, "voice": data_bot.voice }}
        if status == '✅':
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": data_bot.photo,
                    "video": False,
                    "voice": data_bot.voice
                    }
                }
            }
        else:
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": data_bot.photo,
                    "video": True,
                    "voice": data_bot.voice
                    }
                }
            }
        mycol.update_one(last_data, photo_status)

    async def voice_handler(self, status: str, id_bot: int):
        data_bot = self.get_data_bot(id_bot).kirimchannel
        last_data = {"kirimchannel": {"photo": data_bot.photo, "video": data_bot.video, "voice": data_bot.voice }}
        if status == '✅':
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": data_bot.photo,
                    "video": data_bot.video,
                    "voice": False
                    }
                }
            }
        else:
            photo_status = {
                "$set": {"kirimchannel": {
                    "photo": data_bot.photo,
                    "video": data_bot.video,
                    "voice": True
                    }
                }
            }
        mycol.update_one(last_data, photo_status)

    def get_pelanggan(self):
        user_id = []
        for doc in mycol.find():
            user_id.append(doc['_id'])
        
        return get_pelanggan(user_id)

    def get_data_pelanggan(self):
        found = mycol.find_one({'_id': self.user_id})
        return data_pelanggan(found)

    def get_data_bot(self, id_bot):
        found = mycol.find_one({'_id': id_bot})
        return data_bot(found)

class get_pelanggan():
    def __init__(self, args: list):
        args.remove(args[0])
        self.total_pelanggan = len(args)
        self.id_pelanggan = args
        self.json = { "total_pelanggan": len(args), "id_pelanggan": args }

    def get_data_pelanggan(self, index: int = 0):
        found = mycol.find_one({'_id': self.id_pelanggan[index]})
        if found:
            return data_pelanggan(found)
        else:
            return 'ID tidak ditemukan'
    def __str__(self) -> str:
        return str(json.dumps(self.json, indent=3))

class data_pelanggan():
    def __init__(self, args):
        self.id = args['_id']
        self.nama = str(args['nama'])
        self.mention = f'<a href="tg://user?id={self.id}">{self.nama}</a>'
        self.coin = int(args['coin'].split('_')[0])
        self.coin_full = str(args['coin'])
        self.status = str(args['status'].split('_')[0])
        self.status_full = str(args['status'])
        self.menfess = int(args['menfess'])
        self.all_menfess = int(args['all_menfess'])
        self.sign_up = args['sign_up']
        self.json = args

    def __str__(self) -> str:
        return str(json.dumps(self.json, indent=3))


class data_bot():
    def __init__(self, args):
        super().__init__()
        self.id = args['_id']
        self.bot_status = args['bot_status']
        self.ban = dict(args['ban'])
        self.admin = list(args['admin'])
        self.kirimchannel = kirim_channel(dict(args['kirimchannel']))
        # del args['menfess']
        self.json = args

    def __str__(self) -> str:
        return str(json.dumps(self.json, indent=3))

class kirim_channel():
    def __init__(self, args):
        self.photo = args['photo']
        self.video = args['video']
        self.voice = args['voice']
        self.json = args
    def __str__(self) -> str:
        return str(json.dumps(self.json, indent=3))
