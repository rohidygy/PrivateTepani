from ubot import *

__MODULE__ = "ɢᴄᴀꜱᴛ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀꜱᴛ

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴜᴄᴀꜱᴛ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ/ᴋɪʀɪᴍ ᴘᴇꜱᴀɴ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴘᴇɴɢɪʀɪᴍ ᴘᴇꜱᴀɴ ᴋᴇ ꜱᴇᴍᴜᴀ ᴘᴇɴɢɢᴜɴᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ɢᴄᴀꜱᴛ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ/ᴋɪʀɪᴍ ᴘᴇꜱᴀɴ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴘᴇɴɢɪʀɪᴍ ᴘᴇꜱᴀɴ ᴋᴇ ꜱᴇᴍᴜᴀ ɢʀᴜᴘ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ꜱɢᴄᴀꜱᴛ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏꜱᴇꜱ ɢᴄᴀꜱᴛ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ꜱᴇɴᴅ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀ_ɪᴅ - ᴛᴇᴋꜱ/ʀᴇᴘʟʏ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇꜱᴀɴ ᴋᴇ ᴘᴇɴɢɢᴜɴᴀ/ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ.
  
⌑ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴜᴛᴛᴏɴ ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ : <ᴄᴏᴅᴇ> ᴛᴇᴋꜱ ~ ʙᴜᴛᴛᴏɴ_ᴛᴇᴋꜱ:ʙᴜᴛᴛᴏɴ_ᴜʀʟ</ᴄᴏᴅᴇ>
"""


@PY.UBOT("gcast", sudo=True)
async def _(client, message):
    await broadcast_group_cmd(client, message)


@PY.UBOT("ucast", sudo=True)
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.UBOT("sgcast", sudo=True)
async def _(client, message):
    await cancel_broadcast(client, message)


@PY.UBOT("send", sudo=True)
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)


@PY.INLINE("^gcast_button")
@INLINE.QUERY
async def _(client, inline_query):
    await gcast_inline(client, inline_query)
