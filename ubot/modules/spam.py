from ubot import *

__MODULE__ = "ꜱᴘᴀᴍ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴘᴀᴍ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴅꜱᴘᴀᴍ</ᴄᴏᴅᴇ> [ᴊᴜᴍʟᴀʜ] [ᴡᴀᴋᴛᴜ ᴅᴇʟᴀʏ] [ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴅᴇʟᴀʏ ꜱᴘᴀᴍ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴘᴀᴍ</ᴄᴏᴅᴇ> [ᴊᴜᴍʟᴀʜ] [ᴋᴀᴛᴀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ꜱᴘᴀᴍ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴅꜱᴘᴀᴍꜰᴡ</ᴄᴏᴅᴇ> [ᴊᴜᴍʟᴀʜ] [ᴡᴀᴋᴛᴜ] [ʟɪɴᴋ ᴄʜᴀɴɴᴇʟ ᴘᴜʙʟɪᴋ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴅᴇʟᴀʏ ꜱᴘᴀᴍ ꜰᴏʀᴡᴀʀᴅ ʟɪɴᴋ ᴄʜᴀɴɴᴇʟ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴄꜱᴘᴀᴍ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ꜱᴛᴏᴘ ꜱᴘᴀᴍ.
"""


@PY.UBOT("spam|dspam|dspamfw", sudo=True)
async def _(client, message):
    if message.command[0] == "spam":
        await spam_cmd(client, message)
    if message.command[0] == "dspam":
        await dspam_cmd(client, message)
    if message.command[0] == "dspamfw":
        await dspam_fwd(client, message)


@PY.UBOT("cspam", sudo=True)
async def _(client, message):
    await capek_dah(client, message)
