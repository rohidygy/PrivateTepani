from ubot import *

__MODULE__ = "ᴇᴍᴏᴊɪ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴇᴍᴏᴊɪ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴇᴛᴇᴍᴏ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴇᴍᴏᴊɪ ᴘɪɴɢ.

⌑ ​🇵​​🇪​​🇷​​🇮​​🇳​​🇹​​🇦​​🇭​⦂ <​🇨​​🇴​​🇩​​🇪​>{0️⃣}​🇸​​🇪​​🇹​​🇪​​🇲​​🇴​2️⃣</​🇨​​🇴​​🇩​​🇪​>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴇᴍᴏᴊɪ ᴘɪɴɢ.
"""


@PY.UBOT("ping", sudo=True)
@ubot.on_message(filters.user(USER_ID) & filters.command("ping", "^") & ~filters.me)
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
