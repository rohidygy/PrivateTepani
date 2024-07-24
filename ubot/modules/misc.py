__MODULE__ = "ꜱᴜᴅᴏ"
__HELP__ = """
Bantuan Untuk Sudo

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴀᴅᴅꜱᴜᴅᴏ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ɪᴅ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴛᴀᴍʙᴀʜ ᴘᴇɴɢɢᴜɴᴀ ꜱᴜᴅᴏ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴅᴇʟꜱᴜᴅᴏ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ɪᴅ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ʜᴀᴘᴜꜱ ᴘᴇɴɢɢᴜɴᴀ ꜱᴜᴅᴏ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴜᴅᴏʟɪꜱᴛ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴄᴇᴋ ᴘᴇɴɢɢᴜɴᴀ ꜱᴜᴅᴏ.
"""


from pyrogram.enums import *
from pyrogram.types import *

from ubot import *


@PY.UBOT("addsudo", sudo=True)
async def _(client, message):
    msg = await message.reply(f"<b>Processing...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(f"<b>Silakan balas pesan pengguna/username/user id</b>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = monggo.get_list_from_var(client.me.id, "SUDO_USER", "ID_NYA")

    if user.id in sudo_users:
        return await msg.edit(
            f"<b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Sudah menjadi pengguna sudo.</b>"
        )

    try:
        monggo.add_to_var(client.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(
            f"<b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Ditambahkan ke pengguna sudo.</b>"
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("delsudo", sudo=True)
async def _(client, message):
    msg = await message.reply(f"<b>Processing...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply(
            f"<b>Silakan balas pesan penggjna/username/user id.</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = monggo.get_list_from_var(client.me.id, "SUDO_USER", "ID_NYA")

    if user.id not in sudo_users:
        return await msg.edit(
            f"<b>{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Bukan bagian pengguna sudo.</b>"
        )

    try:
        monggo.remove_from_var(client.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(
            f"<b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Dihapus dari pengguna sudo.</b>"
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("sudolist", sudo=True)
async def _(client, message):
    msg = await message.reply(f"<b>Processing...</b>")
    sudo_users = monggo.get_list_from_var(client.me.id, "SUDO_USER", "ID_NYA")

    if not sudo_users:
        return await msg.edit(f"<b>Tidak ada pengguna sudo ditemukan.</b>")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(
                f" • [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code>"
            )
        except:
            continue

    if sudo_list:
        response = (
            f"<b>Daftar Pengguna:</b>\n"
            + "\n".join(sudo_list)
            + f"\n<b> • </b> <code>{len(sudo_list)}</code>"
        )
        return await msg.edit(response)
    else:
        return await msg.edit("<b>Eror</b>")
