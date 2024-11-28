from ubot import *



async def cb_tutor(client, callback_query):
    await callback_query.edit_message_text(
        text="""
<b>sɪʟᴀᴋᴀɴ ʜᴜʙᴜɴɢɪ ᴘᴇᴍɪʟɪᴋ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ :

❐ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴅᴜᴋᴀɴ ᴋᴇʟᴜʜᴀɴ ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ ɪɴɪ</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🥷 ᴏᴡɴᴇʀ", url="https://t.me/kagebunshiiin"),
                    InlineKeyboardButton("📬 ᴋᴏᴛᴀᴋ ᴘᴇsᴀɴ", callback_data="suportkage"),
                ],
                [
                    InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="start0"),
                ],
            ]
        ),
    )

async def diskusi(client, callback_query):
    await callback_query.edit_message_text(
        text="""<b>ɪɴɪ ʟᴀʜ ᴄʜᴀɴᴇʟ ᴏᴡɴᴇʀ ᴅᴀʀɪ ʙᴏᴛ ɪɴɪ</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🖲 ᴏᴡɴᴇʀ ᴄʜᴀɴᴇʟ", url="https://t.me/kagestore69"),
                ],
                [
                    InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="start0"),
                ],
            ]
        ),
    )

async def informasi(client, callback_query):
    await callback_query.edit_message_text(
        text="""
🧰 ᴛᴇɴᴛᴀɴɢ <b>kage ᴅᴇᴠs ʟᴠ</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="start0"),
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

