from ubot import *

__MODULE__ = "ᴍᴇɴᴛɪᴏɴ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴᴛɪᴏɴ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴀʟʟ</ᴄᴏᴅᴇ> [ᴛʏᴘᴇ ᴍᴇꜱꜱᴀɢᴇ/ʀᴇᴘʟʏ ᴍᴇꜱꜱᴀɢᴇ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍᴇɴᴛɪᴏɴ ꜱᴇᴍᴜᴀ ᴀɴɢɢᴏᴛᴀ ɢʀᴜᴘ ᴅᴇɴɢᴀɴ ᴘᴇꜱᴀɴ ʏᴀɴɢ ᴀɴᴅᴀ ɪɴɢɪɴᴋᴀɴ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ʙᴀᴛᴀʟ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴍᴇᴍᴇɴᴛɪᴏɴ ᴀɴɢɢᴏᴛᴀ ɢʀᴜᴘ.
"""


@PY.UBOT("all", sudo=True)
async def _(client, message):
    await mentionall(client, message)


@PY.UBOT("batal", sudo=True)
async def _(client, message):
    await batal_tag(client, message)
