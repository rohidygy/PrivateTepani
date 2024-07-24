from ubot import *

__MODULE__ = "ɪɴᴠɪᴛᴇ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴᴠɪᴛᴇ

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ɪɴᴠɪᴛᴇ</ᴄᴏᴅᴇ> [ᴜꜱᴇʀɴᴀᴍᴇ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴋᴇ ɢʀᴜᴘ.
  """


@PY.UBOT("invite", sudo=True)
async def _(client, message):
    await invite_cmd(client, message)


@PY.UBOT("inviteall", sudo=True)
async def _(client, message):
    await inviteall_cmd(client, message)


@PY.UBOT("cancel", sudo=True)
async def _(client, message):
    await cancel_cmd(client, message)
