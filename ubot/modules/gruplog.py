__MODULE__ = "ɢʀᴜᴘ ʟᴏɢ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʀᴜᴘʟᴏɢꜱ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ʟᴏɢɢᴇʀ</ᴄᴏᴅᴇ> [ᴏɴ/ᴏꜰꜰ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴀᴋᴛɪꜰᴋᴀɴ ᴛᴀɢ ʟᴏɢ ᴅᴀɴ ᴘᴍ ʟᴏɢ.
"""

import asyncio
from pyrogram.errors import FloodWait, UserRestricted, ChannelInvalid
from pyrogram.enums import *
from pyrogram.types import *

from ubot import *


@PY.COSTUM_CMD("LOGS_PM_GROUP", ubot)
async def _(client, message):
    log = monggo.get_var(client.me.id, "TAG_LOG")
    if not log:
        return
    if message.chat.id == 777000:
            return
    from_user = (message.chat if message.chat.type == ChatType.PRIVATE else message.from_user)
    if message.sender_chat:
      if message.sender_chat.username is None:
        user_link = f"{message.sender_chat.title}"
      else:
        user_link = f"[{message.sender_chat.title}](https://t.me/{message.sender_chat.username}"
    else:
      user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
    message_link = (message.link if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP) else f"tg://openmessage?user_id={from_user.id}&message_id={message.id}")
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        text = f"""
📨 <b><u>Group Notifications</u></b>

• <b>Name Group: {message.chat.title}</b>
• <b>ID Group:</b> <code>{message.chat.id}</code>
• <b>Dari: {user_link}</b>
• <b>Pesan:</b> <blockquote>{message.text}</blockquote>
• <b>Tautan Grup: [Disini]({message_link}) </blockquote>
"""
        try:
            await client.send_message(int(log),text,disable_web_page_preview=True)
            await asyncio.sleep(0.5)
        except ChannelInvalid:
            monggo.remove_var(client.me.id, "TAG_LOG")
            return
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await client.send_message(int(log),text,disable_web_page_preview=True)
            await asyncio.sleep(0.5)
    else:
        text = f"""
📨 <b><u>Private Notifications</u></b>

• <b>Dari: {user_link}</b>
• <b>Pesan:</b> <blockquote>{message.text}</blockquote>
• <b>Tautan Pesan: [Disini]({message_link}) </b>
"""
        try:
            await client.send_message(int(log), text,   disable_web_page_preview=True)
            await asyncio.sleep(0.5)
            await message.forward(int(log))
        except Exception:
            return
        except ChannelInvalid:
            monggo.remove_var(client.me.id, "TAG_LOG")
            return
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await client.send_message(int(log),text,disable_web_page_preview=True)
            await asyncio.sleep(0.5)
            await message.forward(int(log))


@PY.UBOT("logger", sudo=True)
async def _(client, message):
    xx = await message.reply(f"**Processing...**")
    cek = get_arg(message)
    logs = monggo.get_var(client.me.id, "TAG_LOG")
    if cek.lower() == "on":
        if not logs:
            try:
                pr = await create_botlog(client)
            except UserRestricted:
                return await xx.edit("<b> Maaf akun anda sedang dibatasi, anda tidak bisa membuat grup log hingga akun anda bebas!!</b>")
            babi = await client.export_chat_invite_link(int(pr))
            monggo.set_var(client.me.id, "TAG_LOG", int(pr))
            return await xx.edit(f"**Log Group Berhasil Diaktifkan :\n\n{babi}**")
        else:
            return await xx.edit(f"**Log Group Anda Sudah Aktif.**")
    if cek.lower() == "off":
        if logs:
            ah = monggo.get_var(client.me.id, "TAG_LOG")
            await client.delete_supergroup(int(ah))
            return await xx.edit(f"**Log Group Berhasil Dinonaktifkan.**")
        else:
            return await xx.edit(f"**Log Group Anda Sudah Dinonaktifkan.**")
    else:
        return await xx.edit(
            f"**Format yang anda berikan salah. silahkan gunakan <code>{message.text} on/off</code>**"
        )
