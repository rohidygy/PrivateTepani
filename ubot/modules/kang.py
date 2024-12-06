from ubot import *

__MODULE__ = "Kang"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴀɴɢ

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴋᴀɴɢ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴋᴇ ꜱᴛɪᴋᴇʀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴋᴏꜱᴜᴍ ꜱᴛɪᴋᴇʀ ᴘᴀᴋ
"""


# @PY.BOT("kang", sudo=True)
# async def _(client, message):
# await kang_cmd_bot(client, message)


@PY.UBOT("kang", sudo=True)
async def _(client, message):
    await kang(client, message)
