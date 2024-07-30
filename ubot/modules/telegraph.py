from ubot import *

__MODULE__ = "ᴛᴇʟᴇɢʀᴀᴘʜ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʟᴇɢʀᴀᴘʜ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴛɢ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ ᴋᴇ ᴛᴇʟᴇɢʀᴀ.ᴘʜ.
"""


@PY.UBOT("tg", sudo=True)
async def _(client, message):
    await tg_cmd(client, message)
