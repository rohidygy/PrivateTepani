from ubot import *

__MODULE__ = "SangMata"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴀɴɢᴍᴀᴛᴀ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{ᴄᴏʙᴀᴅᴀʜ}ꜱɢ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀ_ɪᴅ/ʀᴇᴘʟʏ ᴜꜱᴇʀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍᴇʀɪᴋꜱᴀ ʜɪꜱᴛᴏʀɪ ɴᴀᴍᴀ/ᴜꜱᴇʀɴᴀᴍᴇ.
"""


@PY.UBOT("sg", sudo=True)
async def _(client, message):
    await sg_cmd(client, message)
