from ubot import *

__MODULE__ = "Join"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴ
 
⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴋɪᴄᴋᴍᴇ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴊᴏɪɴ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀɴᴀᴍᴇ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ɢʀᴜᴘ ᴅᴇɴɢᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʟᴇᴀᴠᴇᴀʟʟɢᴄ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ꜱᴇᴍᴜᴀ ᴅᴀʀɪ ɢʀᴜᴘ ᴀᴋᴜɴ ᴀɴᴅᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʟᴇᴀᴠᴇᴀʟʟᴄʜ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ꜱᴇᴍᴜᴀ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴀᴋᴜɴ ᴀɴᴅᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ʟᴇᴀᴠᴇ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀɴᴀᴍᴇ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ᴅᴇɴɢᴀɴ ᴜꜱᴇʀɴᴀᴍᴇ.
"""


@PY.UBOT("kickme|leave", sudo=True)
async def _(client, message):
    await leave(client, message)


@PY.UBOT("join", sudo=True)
async def _(client, message):
    await join(client, message)


@PY.UBOT("leaveallgc", sudo=True)
async def _(client, message):
    await kickmeall(client, message)


@PY.UBOT("leaveallch", sudo=True)
async def _(client, message):
    await kickmeallch(client, message)
