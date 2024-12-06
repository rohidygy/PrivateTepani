from ubot import *

__MODULE__ = "Profile"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏꜰɪʟᴇ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴀᴅᴍɪɴʟɪꜱᴛ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ꜱᴛᴀᴛᴜꜱ ᴀᴅᴍɪɴ ɢʀᴜᴘ ᴀɴᴅᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴇᴛʙɪᴏ</ᴄᴏᴅᴇ> [Qᴜᴇʀʏ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ʙɪᴏ ᴀɴᴅᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴇᴛɴᴀᴍᴇ</ᴄᴏᴅᴇ> [Qᴜᴇʀʏ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ɴᴀᴍᴀ ᴀɴᴅᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴇᴛᴘᴘ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴍᴇᴅɪᴀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ꜰᴏᴛᴏ ᴀᴋᴜɴ ᴀɴᴅᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ʙʟᴏᴄᴋ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴘᴇɴɢɢᴜɴᴀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴜɴʙʟᴏᴄᴋ</ᴄᴏᴅᴇ> [Qᴜᴇʀʏ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ʙᴜᴋᴀ ʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ.
"""


@PY.UBOT("setbio", sudo=True)
async def _(client, message):
    await set_bio(client, message)


@PY.UBOT("setname", sudo=True)
async def _(client, message):
    await setname(client, message)


@PY.UBOT("block", sudo=True)
async def _(client, message):
    await block_user_func(client, message)


@PY.UBOT("unblock", sudo=True)
async def _(client, message):
    await unblock_user_func(client, message)


@PY.UBOT("setpp", sudo=True)
async def _(client, message):
    await set_pfp(client, message)


@PY.UBOT("adminlist", sudo=True)
async def _(client, message):
    await list_admin(client, message)
