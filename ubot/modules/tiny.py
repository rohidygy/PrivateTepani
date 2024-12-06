from ubot import *

__MODULE__ = "Tiny"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪɴʏ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴛɪɴʏ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ ᴛᴏ ꜱᴛɪᴄᴋᴇʀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ꜱᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ᴋᴇᴄɪʟ.
"""


@PY.UBOT("tiny", sudo=True)
async def _(client, message):
    await tiny_cmd(client, message)
