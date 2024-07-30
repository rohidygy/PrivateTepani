from ubot import *

__MODULE__ = "ᴡᴇʙꜱʜᴏᴛ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡᴇʙꜱʜᴏᴛ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱꜱ</ᴄᴏᴅᴇ> [ʟɪɴᴋ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴅᴀʀɪ ʟɪɴᴋ ᴛᴇʀꜱᴇʙᴜᴛ.
"""


@PY.UBOT("ss", sudo=True)
async def _(client, message):
    await take_ss(client, message)
