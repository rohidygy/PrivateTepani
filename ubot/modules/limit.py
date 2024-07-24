from ubot import *

__MODULE__ = "ʟɪᴍɪᴛ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟɪᴍɪᴛ

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʟɪᴍɪᴛ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴄᴇᴋ ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛᴇʀʙᴀᴛᴀꜱ ᴀᴛᴀᴜ ᴛɪᴅᴀᴋ.
"""


@PY.UBOT("limit", sudo=True)
async def _(client, message):
    await limit_cmd(client, message)
