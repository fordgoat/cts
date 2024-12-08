import config

from pyrogram import Client, types, enums
from plugins import Helper, Database

async def start_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = first if not last else first + ' ' + last
    username = '@ctsindo' if not msg.from_user.username else '@' + msg.from_user.username
    mention = msg.from_user.mention
    await msg.reply_text(
        text = config.start_msg.format(
            id = msg.from_user.id,
            mention = mention,
            username = username,
            first_name = await helper.escapeHTML(first),
            last_name = await helper.escapeHTML(last),
            fullname = await helper.escapeHTML(fullname),
            ),
        disable_web_page_preview = True,
        quote = True
    )

async def status_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    db = Database(msg.from_user.id).get_data_pelanggan()
    pesan = '<b>🏷Info user</b>\n'
    pesan += f'├ID : <code>{db.id}</code>\n'
    pesan += f'├Nama : {db.mention}\n'
    pesan += f'└Status : {db.status}\n\n'
    pesan += '<b>📝Lainnya</b>\n'
    pesan += f'├Coin : {helper.formatrupiah(db.coin)}💰\n'
    pesan += f'├Menfess : {db.menfess}/{config.batas_kirim}\n'
    pesan += f'├Semua Menfess : {db.all_menfess}\n'
    pesan += f'└Bergabung : {db.sign_up}'
    await msg.reply(pesan, True, enums.ParseMode.HTML)

async def statistik_handler(client: Helper, id_bot: int):
    db = Database(client.user_id)
    bot = db.get_data_bot(id_bot)
    pesan = "<b>📊 STATISTIK BOT\n\n"
    pesan += f"▪️Pelanggan: {db.get_pelanggan().total_pelanggan}\n"
    pesan += f"▪️Admin: {len(bot.admin)}\n"
    pesan += f"▪️Banned: {len(bot.ban)}\n\n"
    pesan += f"🔰Status bot: {'AKTIF' if bot.bot_status else 'TIDAK AKTIF'}</b>"
    await client.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_admin_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    pesan = "<b>Owner bot</b>\n"
    pesan += "• ID: " + str(config.id_admin) + " | <a href='tg://user?id=" + str(config.id_admin) + "'>Owner bot</a>\n\n"
    if len(db.admin) > 0:
        pesan += "<b>Daftar Admin bot</b>\n"
        ind = 1
        for i in db.admin:
            pesan += "• ID: " + str(i) + " | <a href='tg://user?id=" + str(i) + "'>Admin " + str(ind) + "</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_ban_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    if len(db.ban) == 0:
        return await helper.message.reply_text('<i>Tidak ada user dibanned saat ini</i>', True, enums.ParseMode.HTML)
    else:
        pesan = "<b>Daftar banned</b>\n"
        ind = 1
        for i in db.ban:
            pesan += "• ID: " + str(i) + " | <a href='tg://openmessage?user_id=" + str(i) + "'>( " + str(ind) + " )</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def gagal_kirim_handler(client: Client, msg: types.Message):
    anu = Helper(client, msg)
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    fullname = first_name if not last_name else first_name + ' ' + last_name
    username = '@reonisme' if not msg.from_user.username else '@' + msg.from_user.username
    mention = msg.from_user.mention
    return await msg.reply(config.gagalkirim_msg.format(
        id = msg.from_user.id,
        mention = mention,
        username = username,
        first_name = await anu.escapeHTML(first_name),
        last_name = await anu.escapeHTML(last_name),
        fullname = await anu.escapeHTML(fullname)
    ), True, enums.ParseMode.HTML, disable_web_page_preview=True)

async def help_handler(client, msg):
    db = Database(msg.from_user.id)
    member = db.get_data_pelanggan()
    pesan = "❏ Supported commands\n"
    pesan += '├ • /status — melihat status\n'
    pesan += '└ • /tf_coin — transfer coin ke user lain\n'
    pesan += '\nuntuk mengirim pesan/foto & video gunakan hastag dibawah:\n'
    pesan += '#ctsboy - untuk identitas cowo\n'
    pesan += '#ctsgirl - untuk identitas cewe\n'
    pesan += '#ctsask - digunakan untuk bertanya\n'
    pesan += '#ctsspill - spill sesuatu\n'
    pesan += '#ctsrandom - untuk kirim foto/video random\n'
    pesan += '#ctsstory - untuk bercerita\n'
    pesan += '\ninfo pengaduan atau top up coin hubungi @othentix\n'
    if member.status == 'admin':
        pesan += '\nHanya Admin\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/list_admin — melihat list admin\n'
        pesan += '/list_ban — melihat list banned\n\n'
        pesan += 'Perintah banned\n'
        pesan += '/ban — ban user\n'
        pesan += '/unban — unban user\n'
    if member.status == 'owner':
        pesan += '\n=====OWNER COMMAND=====\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/list_admin — melihat list admin\n'
        pesan += '/list_ban — melihat list banned\n'
        pesan += '/stats — melihat statistik bot\n'
        pesan += '/bot — setbot (on|off)\n'
        pesan += '\n=====BROADCAST OWNER=====\n'
        pesan += '/broadcast — mengirim pesan broadcast kesemua user\n'
        pesan += '/admin — menambahkan admin baru\n'
        pesan += '/unadmin — menghapus admin\n'
        pesan += '/list_ban — melihat list banned\n'
        pesan += '\n=====BANNED COMMAND=====\n'
        pesan += '/ban — ban user\n'
        pesan += '/unban — unban user\n'
    await msg.reply(pesan, True)
