import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://kikoy:kikoy6969@cluster0.vooxu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("DB_NAME", "pot1") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001940437648"))
channel_2 = int(os.getenv("CHANNEL_2", "-1001962418199")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1002110504220"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "5"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "25"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#8888 #2211 #Boy #Girl #Ask #Spill #Random #Story").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """💬 #1 𝗣𝗢𝗧 𝗠𝗲𝗻𝗳𝗲𝘀𝘀 base tempat untuk mengirim pesan, confess, random menfess, pap/video random atau keseharian kalian yang akan dikirim ke @MenfessPOT

𝗖𝗔𝗥𝗔 𝗠𝗘𝗡𝗙𝗘𝗦𝗦 : 
Read https://t.me/MenfessPOT/9, bisa digunakan untuk mengirim pesan (teks, foto dan video).
𝗕𝗔𝗖𝗔 𝗥𝗨𝗟𝗘𝗦 : https://t.me/MenfessPOT/11

need help? contact @othentix
""")
start_msg = os.getenv("START_MSG", """
𝗦𝗲𝗹𝗮𝗺𝗮𝘁 𝗱𝗮𝘁𝗮𝗻𝗴 {mention} 😻

bot promote yang dapat digunakan untuk mencari teman, pacar, dll serta dapat digunakan untuk mengirim pesan berupa foto dan video, gunakan hastag dibawah untuk mengirim pesan:

#Boy - untuk identitas cowo
#Girl - untuk identitas cewe
#Ask - digunakan untuk bertanya
#Spill - spill sesuatu
#Random - untuk kirim foto/video random
#Story - untuk bercerita
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#Boy - untuk identitas cowo
#Girl - untuk identitas cewe
#Ask - digunakan untuk bertanya
#Spill - spill sesuatu
#Random - untuk kirim foto/video random
#Story - untuk bercerita

jangan lupa join @TopGroupChat
""")
