from ubot import *

__MODULE__ = "Google"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴏᴏɢʟᴇ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ɢᴏᴏɢʟᴇ</ᴄᴏᴅᴇ> [Qᴜᴇʀʏ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ꜱᴏᴍᴇᴛʜɪɴɢ.
"""


@PY.UBOT("google", sudo=True)
async def _(client, message):
    await gsearch(client, message)
