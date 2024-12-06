from ubot import *

__MODULE__ = "Memifi"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍɪꜰʏ

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴍᴍꜰ</ᴄᴏᴅᴇ> [ᴛᴇᴋꜱ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴀᴍʙᴀʀ ᴍᴇɴᴊᴀᴅɪ ᴋᴇᴄɪʟ.
"""


@PY.UBOT("mmf|memify", sudo=True)
async def _(client, message):
    await memify_cmd(client, message)
