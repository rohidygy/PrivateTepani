from ubot import *

__MODULE__ = "ɪᴍᴀɢᴇ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪᴍᴀɢᴇ

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʀʙɢ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ꜰᴏᴛᴏ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɢᴀᴍʙᴀʀ.

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʙʟᴜʀ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ꜰᴏᴛᴏ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ʙʟᴜʀ ᴋᴇ ɢᴀᴍʙᴀʀ.

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴍɪʀᴏʀ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ꜰᴏᴛᴏ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ᴄᴇʀᴍɪɴ ᴋᴇ ɢᴀᴍʙᴀʀ.

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ɴᴇɢᴀᴛɪᴠᴇ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ꜰᴏᴛᴏ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ɴᴇɢᴀᴛɪᴠᴇ ᴋᴇ ɢᴀᴍʙᴀʀ.
"""


@PY.UBOT("rbg", sudo=True)
async def _(client, message):
    await rbg_cmd(client, message)


@PY.UBOT("blur", sudo=True)
async def _(client, message):
    await blur_cmd(client, message)


@PY.UBOT("negative", sudo=True)
async def _(client, message):
    await negative_cmd(client, message)


@PY.UBOT("miror", sudo=True)
async def _(client, message):
    await miror_cmd(client, message)
