from ubot import *

__MODULE__ = "Secret"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴇᴄʀᴇᴛ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴍꜱɢ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ - ᴛᴇxᴛ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇꜱᴀɴ ꜱᴇᴄᴀʀᴀ ʀᴀʜᴀꜱɪᴀ.
"""


@PY.UBOT("msg", sudo=True)
async def _(client, message):
    await msg_cmd(client, message)


@PY.INLINE("^secret")
@INLINE.QUERY
async def _(client, inline_query):
    await secret_inline(client, inline_query)
