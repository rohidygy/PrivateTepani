from ubot import *

__MODULE__ = "ʏᴏᴜᴛᴜʙᴇ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʏᴏᴜᴛᴜʙᴇ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴏɴɢ</ᴄᴏᴅᴇ> [ꜱᴏɴɢ ᴛɪᴛʟᴇ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜꜱɪᴄ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴠꜱᴏɴɢ</ᴄᴏᴅᴇ> [ᴠɪᴅᴇᴏ ᴛɪᴛʟᴇ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ.
"""


@PY.UBOT("vsong", sudo=True)
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song", sudo=True)
async def _(client, message):
    await song_cmd(client, message)
