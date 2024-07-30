from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ubot import *


class MSG:
    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ Pemberitahuan</b>
<b>├ Akun :</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ID:</b> <code>{X.me.id}</code>
<b>╰ Masa Aktif Habis</b>
"""

    def START(message):
        if not message.from_user.id == USER_ID:
            msg = f"""
<b>👋🏻 ʜᴀʟᴏ {message.from_user.first_name} !!

💎 ᴀᴘᴀ ᴀᴅᴀ ʏᴀɴɢ ʙɪꜱᴀ ꜱᴀʏᴀ ʙᴀɴᴛᴜ ? ᴊɪᴋᴀ ᴋᴀᴍᴜ ꜱᴜᴅᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ꜱɪʟᴀᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ.</b>
"""
        else:
            msg = f"""
🧑‍💻 Developer <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>

✅ Gunakan Dengan Bijak !!!
"""
        return msg

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<b>Silakan Lakukan Pembayaran Terlebih Dahulu</b>

<b>Harga Perbulan: {harga}.000</b>

<b>💳 Metode Pembayaran:</b>
 ├─• Channel Pembayaran : [Klik Disini](https://t.me/kagestore69)

<b>🔖 Total Harga: ʀᴘ {total}.000</b>
<b>🗓️ Total Bulan: {bulan}</b> 

<b>✅ Klik Tombol Di Bawah Ini Untuk Mengirimkan Bukti Pembayaran</b>
"""
    async def USERBOT(count):
        expired_date = monggo.get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<b>❏ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ ᴇxᴘɪʀᴇᴅ</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""
    def POLICY():
        return """
<b> ⌑ Satelit Bot ⌑ </b>

<b>Kebijakan Pengembalian</b>
Minimal Baca Tod Biar Gak Koar Koar

🆘 Dukungan
Untuk mendapatkan dukungan, Anda dapat:
❏ Mengikuti prosedur pembelian dibot ini
❏ Resiko userbot bisa [Baca Disini](https://t.me/rawatnokos/63)
❏ Beli Userbot = SETUJU DAN PAHAM RESIKO

👉🏻 Tekan tombol Lanjutkan untuk menyatakan bahwa Anda telah
membaca dan menerima ketentuan ini dan melanjutkan
pembelian. Jika tidak, tekan tombol Batalkan
"""


async def sending_user(user_id):
    await bot.send_message(
        user_id,
        "Silakan Buat Userbot Ulang Anda",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Buat Userbot",
                        callback_data="bahan",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
