from ubot import *

__MODULE__ = "ɢʟᴏʙᴀʟ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʟᴏʙᴀʟ

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ɢʙᴀɴ</CODE> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʙᴀʟᴇꜱ ᴘᴇꜱᴀɴ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ.

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴜɴɢʙᴀɴ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʙᴀʟᴇꜱ ᴘᴇꜱᴀɴ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ.

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʟɪꜱᴛɢʙᴀɴ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʙᴀʟᴇꜱ ᴘᴇꜱᴀɴ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ ɢʙᴀɴ.
"""


@PY.UBOT("gban", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("cgban", "") & ~filters.me)
async def _(client, message):
    await global_banned(client, message)


@PY.UBOT("ungban", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("cungban", "") & ~filters.me)
async def _(client, message):
    await cung_ban(client, message)


@PY.UBOT("listgban", sudo=True)
async def _(client, message):
    await gbanlist(client, message)
