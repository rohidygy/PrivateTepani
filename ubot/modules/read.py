from ubot import *

__MODULE__ = "Read"
__HELP__ = """
​ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴏᴄʀ

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴏᴄʀ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴍᴇᴅɪᴀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴄᴀ ᴛᴇᴋꜱ ᴅᴀʀɪ ᴍᴇᴅɪᴀ.
"""


@PY.UBOT("ocr", sudo=True)
async def _(client, message):
    await read_cmd(client, message)
