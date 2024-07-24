from ubot import *

__MODULE__ = "ɪɴꜰᴏ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴꜰᴏ

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ɪɴꜰᴏ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ɪɴꜰᴏʀᴍᴀꜱɪ ᴘᴇɴɢɢᴜɴᴀ.

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴄɪɴꜰᴏ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ɪɴꜰᴏʀᴍᴀꜱɪ ᴏʙʀᴏʟᴀɴ.
"""


@PY.UBOT("whois|info", sudo=True)
async def _(client, message):
    await info_cmd(client, message)


@PY.UBOT("cwhois|cinfo", sudo=True)
async def _(client, message):
    await cinfo_cmd(client, message)
