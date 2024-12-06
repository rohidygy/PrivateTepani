from ubot import *

__MODULE__ = "Logo"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢᴏ

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʟᴏɢᴏ</ᴄᴏᴅᴇ> [ᴛᴇᴋꜱ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ꜱᴇʙᴜᴀʜ ʟᴏɢᴏ ᴅᴇɴɢᴀɴ ᴋᴀᴛᴀ ʀᴀɴᴅᴏᴍ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʙʟᴏɢᴏ</ᴄᴏᴅᴇ> [ᴛᴇᴋꜱ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ᴍᴇɴᴊᴀᴅɪ ʜɪᴛᴀᴍ.
"""


@PY.UBOT("blogo|logo", sudo=True)
async def _(client, message):
    await logo_cmd(client, message)
