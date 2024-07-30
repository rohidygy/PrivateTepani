from ubot import *

__MODULE__ = "ᴄʀᴇᴀᴛᴇ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʀᴇᴀᴛᴇ

• ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴄʀᴇᴀᴛᴇ</ᴄᴏᴅᴇ> ɢᴄ
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢʀᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ.

• ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴄʀᴇᴀᴛᴇ</ᴄᴏᴅᴇ> ᴄʜ
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ.
"""


@PY.UBOT("create", sudo=True)
async def _(client, message):
    await buat_apaam(client, message)
