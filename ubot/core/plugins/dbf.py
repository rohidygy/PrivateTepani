from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from ubot import *

# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    message.from_user.id
    user_id, get_bulan = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply(f"<b>{message.text} [user_id/username - bulan]</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await message.reply(str(error))
    if not get_bulan:
        get_bulan = 1
    premium = monggo.cek_prem(get_id)
    if premium:
        return await message.reply(
            f"Pengguna denga ID : `{get_id}` sudah memiliki akses !"
        )
    added = monggo.add_prem(get_id)
    if added:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        expired_formatted = expired.strftime("%d %b %Y")
        monggo.set_expired_date(get_id, expired)
        await message.reply(
            f"✅ {get_id} Berhasil diaktifkan selama `{get_bulan}` bulan."
        )
        await bot.send_message(
            get_id,
            f"Selamat ! Akun anda sudah memiliki akses untuk pembuatan userbot",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Lanjutkan Pembuatan Userbot", callback_data="bahan"
                        )
                    ],
                ]
            ),
        )
        await bot.send_message(
            OWNER_ID,
            f"• {message.from_user.id} ─> {get_id} •",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "👤 ᴘʀᴏғɪʟ",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "ᴘʀᴏғɪʟ 👤", callback_data=f"profil {get_id}"
                        ),
                    ],
                ]
            ),
        )
    else:
        await message.reply_text("Error")


async def unprem_user(client, message):
    user_id = await extract_user(message)
    message.from_user.id
    if not user_id:
        return await message.reply("Balas pesan pengguna atau berikan user_id/username")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await message.reply(str(error))
    delpremium = monggo.cek_prem(user.id)
    if not delpremium:
        return await message.reply("Tidak ditemukan")
    removed = monggo.remove_prem(user.id)
    if removed:
        await message.reply(f" ✅ {user.mention} berhasil dihapus")
    else:
        await message.reply_text("Terjadi kesalahan yang tidak diketahui")


async def get_prem_user(client, message):
    text = ""
    count = 0
    for user_id in monggo.get_prem():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{userlist}\n"
    if not text:
        await message.reply_text("Tidak ada pengguna yang ditemukan")
    else:
        await message.reply_text(text)


# ========================== #
# DATABASE BLACKLIST #
# ========================== #


async def add_blaclist(client, message):
    chat_id = message.chat.id
    blacklist = monggo.get_chat(client.me.id)
    if chat_id in blacklist:
        return await message.reply("Grup ini sudah ada dalam blacklist")
    add_blacklist = monggo.add_chat(client.me.id, chat_id)
    if add_blacklist:
        await message.reply(
            f"{message.chat.title} berhasil ditambahkan ke daftar hitam"
        )
    else:
        await message.reply("Terjadi kesalahan yang tidak diketahui")


async def del_blacklist(client, message):
    try:
        if not get_arg(message):
            chat_id = message.chat.id
        else:
            chat_id = int(message.command[1])
        blacklist = monggo.get_chat(client.me.id)
        if chat_id not in blacklist:
            return await message.reply(
                f"{message.chat.title} tidak ada dalam daftar hitam"
            )
        del_blacklist = monggo.remove_chat(client.me.id, chat_id)
        if del_blacklist:
            await message.reply(f"{chat_id} berhasil dihapus dari daftar hitam")
        else:
            await message.reply("Terjadi kesalahan yang tidak diketahui")
    except Exception as error:
        await message.reply(str(error))


async def get_blacklist(client, message):
    msg = f"<b>• Total blacklist {len(monggo.get_chat(client.me.id))}</b>\n\n"
    for X in monggo.get_chat(client.me.id):
        try:
            get = await client.get_chat(X)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"

    await message.reply(msg)


async def rem_all_blacklist(client, message):
    msg = await message.reply("Sedang Diproses...")
    get_bls = monggo.get_chat(client.me.id)
    if len(get_bls) == 0:
        return await msg.edit("Daftar hitam Anda kosong")
    for X in get_bls:
        monggo.remove_chat(client.me.id, X)
    await msg.edit("Semua daftar hitam telah berhasil dihapus")


# ========================== #
# DATABASE RESELLER #
# ========================== #


async def seles_user(client, message):
    user_id = await extract_user(message)
    message.from_user.id
    if not user_id:
        return await message.reply("Balas pesan pengguna atau berikan user_id/username")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await message.reply(str(error))
    sel = monggo.cek_seles(user.id)
    if sel:
        return await message.reply("Sudah menjadi reseller.")
    added = monggo.add_seles(user.id)
    if added:
        monggo.add_prem(user.id)
        await message.reply(f"✅ {user.mention} telah menjadi reseller")
    else:
        await message.reply_text("Terjadi kesalahan yang tidak diketahui")


async def unseles_user(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("Balas pesan pengguna atau berikan user_id/username")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await message.reply(str(error))
    delreseller = monggo.cek_seles(user.id)
    if not delreseller:
        return await message.reply("Tidak ditemukan")
    removed = monggo.remove_seles(user.id)
    if removed:
        monggo.remove_prem(user.id)
        await message.reply(f"{user.mention} berhasil dihapus")
    else:
        await message.reply_text("Terjadi kesalahan yang tidak diketahui")


async def get_seles_user(client, message):
    text = ""
    count = 0
    if message.from_user.id not in FKM_ID:
        return
    for user_id in monggo.get_seles():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{userlist}\n"
    if not text:
        await message.reply_text("Tidak ada pengguna yang ditemukan")
    else:
        await message.reply_text(text)


# ========================== #
# DATABASE EXPIRED #
# ========================== #


async def expired_add(client, message):
    user_id, get_day = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply(f"{message.text} user_id/username - hari")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await message.reply(str(error))
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    monggo.set_expired_date(user_id, expire_date)
    await message.reply(f"{get_id} telah diaktifkan selama {get_day} hari.")


async def expired_cek(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("Pengguna tidak ditemukan")
    expired_date = monggo.get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"{user_id} belum diaktifkan.")
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(
            f"{user_id} aktif hingga {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. Sisa waktu aktif {remaining_days} hari."
        )


async def un_expired(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("User tidak ditemukan")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await message.reply(str(error))
    monggo.rem_expired_date(user.id)
    return await message.reply(f"✅ {user.id} expired telah dihapus")


async def bacotan(_, message):
    if message.from_user.id not in FKM_ID:
        return
    
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    
    if len(message.command) > 1:
        return await message.reply(
            "<b>Silakan sertakan pesan atau balas pesan yang ingin disiarkan.</b>"
        )

    kntl = 0
    mmk = []
    babi = monggo.get_served_users()
    jmbt = len(babi)

    for xx in babi:
        logging.info(f"xx: {xx}, type of xx: {type(xx)}")

        if isinstance(xx, dict) and "user_id" in xx:
            try:
                mmk.append(int(xx["user_id"]))
            except (TypeError, ValueError) as e:
                logging.error(f"Kesalahan saat mengkonversi user_id ke int: {e}")
        else:
            logging.error(f"xx bukan objek dict atau tidak memiliki kunci 'user_id': {xx}")

    if FKM_ID in mmk:
        mmk.remove(FKM_ID)

    for i in mmk:
        try:
            m = (
                await bot.forward_messages(i, y, x)
                if message.reply_to_message
                else await bot.send_message(i, y, x)
            )
            kntl += 1
        except Exception as e:
            logging.error(f"Kesalahan saat mengirim pesan ke {i}: {e}")

    return await message.reply(
        f"**✅ Berhasil mengirim pesan ke `{kntl}` pengguna, dari `{jmbt}` pengguna.**",
    )
