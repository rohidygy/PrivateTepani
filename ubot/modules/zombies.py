from ubot import *

__MODULE__ = "ᴢᴏᴍʙɪᴇꜱ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴢᴏᴍʙɪᴇꜱ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴢᴏᴍʙɪᴇꜱ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇʟᴜᴀʀᴋᴀɴ ᴀᴋᴜɴ ᴅᴇᴘʀᴇꜱɪ ᴅɪɢʀᴜᴘ ᴀɴᴅᴀ.
"""


@PY.UBOT("zombies", sudo=True)
async def _(client, message):
    await zombies_cmd(client, message)
