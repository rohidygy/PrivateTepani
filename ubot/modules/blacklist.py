from ubot import *

__MODULE__ = "ᴀɴᴛɪɢᴄᴀꜱᴛ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴᴛɪɢᴄᴀꜱᴛ

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴀᴄᴛɪᴠᴇ</ᴄᴏᴅᴇ>
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇɴɢʜᴀᴘᴜꜱ ꜱᴇᴍᴜᴀ ᴀɴᴛɪ ɢᴄᴀꜱᴛ

• Perintah : <code>{0}addbl</code>
• Penjelasan : Menambahkan grup kedalam anti Gcast.

• Perintah : <code>{0}delbl</code>
• Penjelasan : Menghapus grup dari daftar anti Gcast.

• Perintah : <code>{0}listbl</code>
• Penjelasan : Melihat daftar grup anti Gcast.
"""


@PY.UBOT("addbl", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("addbl", "") & ~filters.me)
async def _(client, message):
    await add_blaclist(client, message)


@PY.UBOT("delbl", sudo=True)
async def _(client, message):
    await del_blacklist(client, message)


@PY.UBOT("active", sudo=True)
async def _(client, message):
    await rem_all_blacklist(client, message)


@PY.UBOT("listbl", sudo=True)
async def _(client, message):
    await get_blacklist(client, message)
