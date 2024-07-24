from ubot import *

__MODULE__ = "ᴍᴇᴍᴇ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍᴇ

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴍᴇᴍᴇꜱ</ᴄᴏᴅᴇ> [ᴛᴇᴋꜱ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴋᴀᴛᴀ ᴍᴇᴍᴇꜱ ʀᴀɴᴅᴏᴍ.
"""


@PY.UBOT("mms|memes", sudo=True)
async def _(client, message):
    await memes_cmd(client, message)
