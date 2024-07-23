from pyrogram import *
from pyrogram.types import *

from ubot import *

flood = {}
flood2 = {}

DEFAULT_TEXT = """
<blockquote><b>I am {} maintains this Chat Room . Don't spam or You will be auto blocked.</b></blockquote>
"""

PM_WARN = """
Security Message {} . You have <code>{}/{}</code> warnings !!

{}
"""

LIMIT = 5

async def delete_old_message(message, msg_id):
    try:
        await message._client.delete_messages(message.chat.id, msg_id)
    except:
        pass

async def permitpm(client, message):
    user_id = client.me.id
    babi = await message.reply("`Processing...`")
    bacot = get_arg(message)
    if not bacot:
        return await babi.edit(f"`Gunakan Format : `{0}pmpermit on or off`.`")
    is_already = monggo.get_var(user_id, "ANTI_PM")
    if bacot.lower() == "on":
        if is_already:
            return await babi.edit("`PMPermit Sudah DiHidupkan.`")
        monggo.set_var(user_id, "ANTI_PM", True)
        await babi.edit("`PMPermit Berhasil DiHidupkan.`")
    elif bacot.lower() == "off":
        if not is_already:
            return await babi.edit("`PMPermit Sudah DiMatikan.`")
        monggo.set_var(user_id, "ANTI_PM", False)
        await babi.edit("`PMPermit Berhasil DiMatikan.`")
    else:
        await babi.edit(f"`Gunakan Format : `{0}pmpermit on or off`.`")


async def approve(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    babi = await message.reply(f"{emo.proses} <b>Processing...</b>")
    chat_type = message.chat.type
    getc_pm_warns = monggo.get_var(client.me.id, "PM_LIMIT")
    pm_text = monggo.get_var(client.me.id, "PM_TEXT")
    custom_pm_txt = pm_text if pm_text else DEFAULT_TEXT
    custom_pm_warns = getc_pm_warns if getc_pm_warns else LIMIT
    if chat_type == "me":
        return await babi.edit(f"{emo.gagal} <b>Apakah anda sudah gila ?</b>")
    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not message.reply_to_message:
            return await babi.edit(
                f"{emo.gagal} <b>Balas ke pesan pengguna, untuk disetujui.</b>"
            )
        dia = message.reply_to_message.from_user.id
    elif chat_type == enums.ChatType.PRIVATE:
        dia = message.chat.id
    else:
        return
    ok_tak = monggo.dicek_pc(dia)
    if ok_tak:
        return await babi.edit(f"{emo.sukses} <b>Pengguna ini sudah disetujui.</b>")

    teks, button = get_msg_button(custom_pm_txt)
    button = create_tl_btn(button)
    if button:
        async for m in client.get_chat_history(dia, limit=custom_pm_warns):
            if m.reply_markup:
                await m.delete()
    else:
        try:
            await client.delete_messages(message.chat.id, message_ids=flood2[dia])
        except KeyError:
            pass
        # if dia in flood:
        # try:
        # await client.delete_messages(
        # chat_id, message_ids=flood2[dia])
        # except BaseException:
        # pass
    monggo.oke_pc(dia)
    await babi.edit(
        f"{emo.sukses} <b>Baiklah, pengguna ini disetujui untuk mengirim pesan.</b>"
    )


async def disapprove(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    babi = await message.reply(f"{emo.proses} <b>Processing...</b>")
    await asyncio.sleep(2)
    rep = message.reply_to_message
    chat_type = message.chat.type
    if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not rep:
            return await babi.edit(
                f"{emo.gagal} <b>Balas ke pesan pengguna, untuk ditolak.</b>"
            )
        message.reply_to_message.from_user.id
    elif chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
    else:
        return
    ok_tak = monggo.dicek_pc(user_id)
    if not ok_tak:
        return await babi.edit(
            f"{emo.gagal} <b>Pengguna ini memang belum disetujui untuk mengirim pesan.</b>"
        )
    monggo.tolak_pc(user_id)
    await babi.edit(
        f"{emo.sukses} <b>Baiklah, pengguna ini ditolak untuk mengirim pesan.</b>"
    )


async def get_msg(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    jing = await message.reply(f"{emo.proses} <b>Processing...</b>")
    if len(message.command) < 2:
        return await jing.edit(
            f"{emo.gagal} <b>Tidak ada variabel tersebut !! Variabel : <code>pmpic</code>, <code>pmtext</code>, <code>pmlimit</code>.</b>"
        )
    command, variable = message.command[:2]
    if variable.lower() == "pmtext":
        bb = monggo.get_var(client.me.id, "PM_TEXT")
        cc = bb if bb else DEFAULT_TEXT
        teks, button = get_msg_button(cc)
        if button:
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_teks_but {message.chat.id}"
                )
                await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=ReplyCheck(message),
                )
                await jing.delete()
            except Exception as e:
                await jing.edit(f"Error {e}")
        else:
            await jing.edit(
                f"{emo.sukses} <b>Ini PM Text anda :\n<code>{bb}</code></b>"
            )
    elif variable.lower() == "pmlimit":
        bb = monggo.get_var(client.me.id, "PM_LIMIT")
        await jing.edit(f"{emo.sukses} <b>Ini PM Limit anda :\n<code>{bb}</code></b>")
    elif variable.lower() == "pmpic":
        bb = monggo.get_var(client.me.id, "PM_PIC")
        await jing.edit(f"{emo.sukses} <b>Ini PM Pic anda :\n<code>{bb}</code></b>")
    else:
        await jing.edit(
            f"{emo.gagal} <b>Tidak ada variabel tersebut !! Variabel : <code>pmpic</code>, <code>pmtext</code>, <code>pmlimit</code>.</b>"
        )


async def geteksbut(client, iq):
    gw = iq.from_user.id
    getpm_txt = monggo.get_var(gw, "PM_TEXT")
    pm_text = getpm_txt if getpm_txt else DEFAULT_TEXT
    teks, button = get_msg_button(pm_text)
    button = create_tl_btn(button)
    duar = [
        (
            InlineQueryResultArticle(
                title="Tombol Teks PM!",
                input_message_content=InputTextMessageContent(teks, disable_web_page_preview=True),
                reply_markup=(button),
            )
        )
    ]
    await client.answer_inline_query(iq.id, cache_time=0, results=duar)


async def set_msg(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    babi = await message.reply(f"{emo.proses} <b>Processing...</b>")
    await asyncio.sleep(2)
    user_id = client.me.id
    r_msg = message.reply_to_message
    args_txt = get_arg(message)
    if r_msg:
        if r_msg.text:
            pm_txt = r_msg.text
        else:
            return await babi.edit(
                f"{emo.gagal} <b>Silakan balas ke pesan untuk dijadikan teks PMPermit !</b>"
            )
    elif args_txt:
        pm_txt = args_txt
    else:
        return await babi.edit(
            f"{emo.gagal} <b>Silakan balas ke pesan atau berikan pesan untuk dijadikan teks PMPermit !\nContoh :<code>{message.text} Halo saya anuan.</code></b>"
        )
    monggo.set_var(user_id, "PM_TEXT", pm_txt)
    await babi.edit(
        f"{emo.sukses} <b>Pesan PMPemit berhasil diatur menjadi : <code>{pm_txt}</code>.</b>"
    )


async def set_limit(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    babi = await message.reply(f"{emo.proses} <b>Processing...</b>")
    await asyncio.sleep(2)
    user_id = client.me.id
    args_txt = get_arg(message)
    if args_txt:
        if args_txt.isnumeric():
            pm_warns = int(args_txt)
        else:
            return await babi.edit(
                f"{emo.gagal} <b>Silakan berikan untuk angka limit !</b>"
            )
    else:
        return await babi.edit(
            f"{emo.gagal} <b>Silakan berikan pesan untuk dijadikan angka limit !\nContoh :<code> {message.text}setlimit 5.</code></b>"
        )
    monggo.set_var(user_id, "PM_LIMIT", pm_warns)
    await babi.edit(
        f"{emo.sukses} <b>Pesan Limit berhasil diatur menjadi : <code>{args_txt}</code>.</b>"
    )


async def handle_pmpermit(client, message):
    sibot = await client.get_users(bot.me.username)
    diabot = f"<a href=tg://user?id={sibot.id}>{sibot.first_name} {sibot.last_name or ''}</a>"
    gw = client.me.id
    dia = message.from_user
    okga = monggo.dicek_pc(dia.id)
    pmguard = monggo.get_var(gw, "ANTI_PM")
    getc_pm_txt = monggo.get_var(gw, "PM_TEXT")
    getc_pm_warns = monggo.get_var(gw, "PM_LIMIT")

    custom_pm_txt = getc_pm_txt if getc_pm_txt else DEFAULT_TEXT
    custom_pm_warns = getc_pm_warns if getc_pm_warns else LIMIT
    if not pmguard:
        return

    if okga:
        return
    if dia.is_fake or dia.is_scam:
        await message.reply("**Sepertinya anda mencurigakan...**")
        return await client.block_user(dia.id)
    if dia.is_support or dia.is_verified or dia.is_self:
        return
    if dia.id in DEVS:
        try:
            monggo.oke_pc(dia.id)
            await client.send_message(
                dia.id,
                f"<b>Menerima Pesan Dari {dia.mention} !!\nTerdeteksi Founder Dari {diabot}.</b>",
                parse_mode=enums.ParseMode.HTML,
            )
        except BaseException:
            pass
        return
    if int(dia.id) in flood2:
        await delete_old_message(message, flood2.get(int(dia.id), 0))
    #button = create_tl_btn(button)
    if int(dia.id) in flood:
        flood[int(dia.id)] += 1
    else:
        flood[int(dia.id)] = 1
    if flood[int(dia.id)] > int(custom_pm_warns):
        del flood[int(dia.id)]
        await message.reply_text(f"**SPAM DETECTED, BLOCKED USER AUTOMATICALLY!**")
        return await client.block_user(dia.id)
    monggo.set_flood(gw, dia.id, flood[int(dia.id)])
    teks, button = get_msg_button(custom_pm_txt)
    if button:
        try:
            x = await client.get_inline_bot_results(
                bot.me.username, f"ambil_tombolpc {int(dia.id)}"
            )
            msg = await client.send_inline_bot_result(
                dia.id,
                x.query_id,
                x.results[0].id,
                reply_to_message_id=ReplyCheck(message),
            )
            flood2[int(dia.id)] = int(msg.updates[0].id)
        except Exception as e:
            return await eor(message, f"Error {e}")
    else:
        gmbr = monggo.get_var(gw, "PM_PIC")
        if gmbr:
            kok_poto = (
                message.reply_video if gmbr.endswith(".mp4") else message.reply_photo
            )
            rplied_msg = await kok_poto(
                gmbr,
                caption=PM_WARN.format(
                    client.me.mention,
                    flood[int(dia.id)],
                    custom_pm_warns,
                    custom_pm_txt.format(diabot),
                ),
            )
        else:
            rplied_msg = await message.reply(
                PM_WARN.format(
                    client.me.mention,
                    flood[int(dia.id)],
                    custom_pm_warns,
                    custom_pm_txt.format(diabot),
                )
            )
        flood2[int(dia.id)] = rplied_msg.id



async def pc_inline(client, iq):
    org = iq.query.split()
    gw = iq.from_user.id
    getpm_txt = monggo.get_var(gw, "PM_TEXT")
    getpm_warns = monggo.get_var(gw, "PM_LIMIT")
    pm_warns = getpm_warns if getpm_warns else LIMIT
    pm_text = getpm_txt if getpm_txt else DEFAULT_TEXT
    flood = monggo.get_flood(gw, int(org[1]))
    teks, button = get_msg_button(pm_text)
    button = create_tl_btn(button)
    kiki = PM_WARN.format(iq.from_user.mention,flood,pm_warns,teks.format(bot.me.mention))
    lah = monggo.get_var(gw, "PM_PIC")
    if lah:
        filem = (
            InlineQueryResultVideo if lah.endswith(".mp4") else InlineQueryResultPhoto
        )
        url_ling = (
            {"video_url": lah, "thumb_url": lah}
            if lah.endswith(".mp4")
            else {"photo_url": lah}
        )
        duar = [
            filem(
                **url_ling,
                title="PIC Buttons !",
                caption=kiki,
                reply_markup=(button),
            )
        ]
    else:
        duar = [
            (
                InlineQueryResultArticle(
                    title="Tombol PM!",
                    input_message_content=InputTextMessageContent(kiki, disable_web_page_preview=True),
                    reply_markup=(button),
                )
            )
        ]
    await client.answer_inline_query(iq.id, cache_time=0, results=duar)