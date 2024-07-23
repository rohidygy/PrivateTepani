from ubot import *



async def cb_tutor(client, callback_query):
    await callback_query.edit_message_text(
        text="""
<b>👨🏻‍💻 Silahkan hubungi admin dibawah ini :

❐ untuk bertanya apapun termasuk seputar bot ini</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🥷 ᴏᴡɴᴇʀ", url="https://t.me/rezadevx"),
                    InlineKeyboardButton("📬 ᴋᴏᴛᴀᴋ ᴘᴇsᴀɴ", callback_data="support"),
                ],
                [
                    InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="start0"),
                ],
            ]
        ),
    )

async def diskusi(client, callback_query):
    await callback_query.edit_message_text(
        text="""<b>Dibawah ini adalah Channel Updates APOCO USERBOT</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🔊 Channel", url="https://t.me/xCodee1"),
                ],
                [
                    InlineKeyboardButton(text="Kembali", callback_data="start0"),
                ],
            ]
        ),
    )

async def informasi(client, callback_query):
    await callback_query.edit_message_text(
        text="""
🤖 Tentang <b>Apoco-Userbot</b>

penjelasan tentang <b>userbot</b> bisa [Baca Disini](https://t.me/rawatnokos/61)

<b>Dengan @apocouserbot Anda dapat melakukan hal-hal berikut :</b>
❐ Mengirim pesan ke semua grup / pengguna secara bersamaan
❐ Mengelola dan memoderasi grup
❐ Mengunduh media
❐ Mengonversi format media
❐ Balasan pesan otomatis
❐ Menggunakan Fitur AI
❐ Membuat Sticker
❐ Digunakan untuk Promosi
❐ Melakukan Fake OS / naik ke obrolan suara menggunakan bot
❐ Menyimpan media dari channel yang dibatasi
❐ Menanggapi perintah yang diberikan

...Dan masih banyak lagi!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Kembali", callback_data="start0"),
                ],
            ]
        ),
    )

async def asdksd(client, callback_query):
    if callback_query.from_user.id in DEVS:
        buttons = [
            [InlineKeyboardButton("📌 Buat Userbot", callback_data="bahan")],
            [
                InlineKeyboardButton("💬 Penjelasan", callback_data="informasi"),
                InlineKeyboardButton("☎️ Admin", callback_data="cb_tutor"),
            ],
            [
                InlineKeyboardButton("⚡ Support", callback_data="diskusi"),
                InlineKeyboardButton("⏳ Status Akun", callback_data="start_profile"),
            ],
          ]
    else:
        buttons = [
            [InlineKeyboardButton("📌 Buat Userbot", callback_data="bahan")],
            [
                InlineKeyboardButton("💬 Penjelasan", callback_data="informasi"),
                InlineKeyboardButton("☎️ Admin", callback_data="cb_tutor"),
            ],
            [
                InlineKeyboardButton("⚡ Support", callback_data="diskusi"),
                InlineKeyboardButton("⏳ Status Akun", callback_data="start_profile"),
            ],
          ]
    msg = f"""
<b>👋🏻 ʜᴀʟᴏ {callback_query.from_user.first_name} !!
💎 ᴀᴘᴀ ᴀᴅᴀ ʏᴀɴɢ ʙɪꜱᴀ ꜱᴀʏᴀ ʙᴀɴᴛᴜ ? ᴊɪᴋᴀ ᴋᴀᴍᴜ ꜱᴜᴅᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ꜱɪʟᴀᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ.</b>
"""
    await callback_query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(buttons))
    monggo.add_served_user(callback_query.from_user.id)

