import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID", "29486311"))
api_hash = os.getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
bot_token = os.getenv("BOT_TOKEN", "")
# =========================================================== #

db_url = os.getenv("DB_URL", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("DB_NAME", "cts1") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.getenv("CHANNEL_1", "-1001940437648"))
channel_2 = int(os.getenv("CHANNEL_2", "-1002138039201")) #untuk group comentar user
channel_log = int(os.getenv("CHANNEL_LOG", "-1002110504220"))
# =========================================================== #

id_admin = int(os.getenv("ID_ADMIN", "957521020"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", "3"))
# =========================================================== #

biaya_kirim = int(os.getenv("BIAYA_KIRIM", "25"))
# =========================================================== #

hastag = os.getenv("HASTAG", "#889178 #2211 #ctsboy #ctsgirl #ctsask #ctsspill #ctsrandom #ctsstory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.getenv("PIC_BOY", "https://telegra.ph/file.jpg")
pic_girl = os.getenv("PIC_GIRL", "https://telegra.ph/file.jpg")
# =========================================================== #

pesan_join = os.getenv("PESAN_JOIN", """💬 #1 𝗠𝗘𝗡𝗙𝗘𝗦𝗦 𝗦𝗧𝗔𝗬𝗖𝗔𝗧𝗜𝗢𝗡 base tempat untuk mengirim pesan, confess, random menfess, pap/video random atau keseharian kalian yang akan dikirim ke @MenfessCTS

𝗖𝗔𝗥𝗔 𝗠𝗘𝗡𝗙𝗘𝗦𝗦 : 
Read https://t.me/MenfessCTS/9, bisa digunakan untuk mengirim pesan (teks, foto dan video).
𝗕𝗔𝗖𝗔 𝗥𝗨𝗟𝗘𝗦 : https://t.me/MenfessCTS/11

need help? contact @othentix
""")
start_msg = os.getenv("START_MSG", """
𝗦𝗲𝗹𝗮𝗺𝗮𝘁 𝗱𝗮𝘁𝗮𝗻𝗴 {mention} 😻

bot promote yang dapat digunakan untuk mencari teman, pacar, dll serta dapat digunakan untuk mengirim pesan berupa foto dan video, gunakan hastag dibawah untuk mengirim pesan:

#ctsboy - untuk identitas cowo
#ctsgirl - untuk identitas cewe
#ctsak - digunakan untuk bertanya
#ctsspill - spill sesuatu
#ctsrandom - untuk kirim foto/video random
#ctsstory - untuk bercerita
""")

gagalkirim_msg = os.getenv("GAGAL_KIRIM", """
{mention} pesanmu gagal terkirim 🙅, harap gunakan hastag : 

#ctsboy - untuk identitas cowo
#ctsgirl - untuk identitas cewe
#ctsask - digunakan untuk bertanya
#ctsspill - spill sesuatu
#ctsrandom - untuk kirim foto/video random
#ctsstory - untuk bercerita

jangan lupa join @TopGroupChat
""")
