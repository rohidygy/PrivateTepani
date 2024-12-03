import re

from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait
from pyrogram.types import (InlineQueryResultArticle, InlineQueryResultPhoto,
                            InlineQueryResultVideo, InputTextMessageContent)

from ubot import bot, ubot
from ubot.core.database import monggo
from ubot.core.helpers import (Emo, ReplyCheck, cb_nts_btn, cek_tautan,
                               get_media_type_from_url, get_msg_button)


async def save_note(client: ubot, message):
    emo = Emo(client)
    await emo.init()
    pref = monggo.get_pref(client.me.id)
    x = next(iter(pref))
    cek = message.reply_to_message
    note_name = message.text.split()[1]
    if not note_name:
        return await message.reply(
            f"<blockquote>{emo.gagal} <b>Berikan nama cataran</b></blockquote>"
        )
    gclog = monggo.get_log_group_id(client.me.id)
    logs = gclog if gclog else "me"
    pros = await message.reply(
        f"<blockquote>{emo.proses} <b>Proses simpan catatan ..</b></blockquote>"
    )
    if not note_name or not cek:
        return await pros.edit(
            f"<blockquote>{emo.gagal} <b>Gunakan perintah:</b>\n<code>{x}save</code> [nama catatan] [balas atau berikan pesan].</blockquote>"
        )
    getnotes = monggo.get_var(client.me.id, note_name, "notes")
    if getnotes:
        return await pros.edit(
            "<blockquote><b>Catatan <code>{}</code> sudah ada.</b></blockquote>".format(
                emo.gagal
            )
        )
    value = None
    type_mapping = {
        "text": cek.text,
        "photo": cek.photo,
        "voice": cek.voice,
        "audio": cek.audio,
        "video": cek.video,
        "video_note": cek.video_note,
        "animation": cek.animation,
        "sticker": cek.sticker,
        "document": cek.document,
        "contact": cek.contact,
    }
    for media_type, media in type_mapping.items():
        if media:
            send = await cek.copy(logs)
            value = {
                "type": media_type,
                "message_id": send.id,
            }
            break
    if value:
        monggo.set_var(client.me.id, note_name, value, "notes")
        return await pros.edit(
            f"<blockquote>{emo.sukses} <b>Catatan <code>{note_name}</code> berhasil disimpan.</b></blockquote>"
        )
    else:
        return await pros.edit(
            f"<blockquote>{emo.gagal} <b>Gunakan perintah:</b>\n<code>{x}save</code> [nama catatan] [balas atau berikan pesan].</blockquote>"
        )


async def get_note(client: ubot, message):
    emo = Emo(client)
    await emo.init()
    pros = await message.reply(
        f"<blockquote>{emo.proses} <b>Proses ambil catatan ..</b></blockquote>"
    )
    gclog = monggo.get_log_group_id(client.me.id)
    logs = gclog if gclog else "me"
    if len(message.text.split()) == 2:
        note = message.text.split()[1]
        data = monggo.get_var(client.me.id, note, "notes")
        if not data:
            return await pros.edit(
                f"<blockquote>{emo.gagal} <b>Tidak ada catatan bernama <code>{note}</code></b></blockquote>"
            )
        msg_id = await client.get_messages(logs, int(data["message_id"]))
        return await getnotes_(client, message, pros, note, data, msg_id)
    elif len(message.text.split()) == 3 and (message.text.split())[2] in [
        "noformat",
        "raw",
    ]:
        note = message.text.split()[1]
        data = monggo.get_var(client.me.id, note, "notes")
        if not data:
            return await pros.edit(
                f"<blockquote>{emo.gagal} <b>Tidak ada catatan bernama <code>{note}</code></b></blockquote>"
            )
        msg_id = await client.get_messages(logs, int(data["message_id"]))
        return await get_raw_note(client, message, pros, note, data, msg_id)
    else:
        return await pros.edit(
            f"<blockquote>{emo.gagal} <b>Berikan nama catatan.</b></blockquote>"
        )


async def getnotes_(c, m, xx, note, data, msg_id):
    em = Emo(c)
    await em.init()
    thetext = msg_id.text if msg_id.text else msg_id.caption or ""
    teks, button = get_msg_button(thetext)
    if button:
        try:
            a = await c.get_inline_bot_results(bot.me.username, f"get_note_ {note}")
            await m.delete()
            await c.send_inline_bot_result(
                m.chat.id,
                a.query_id,
                a.results[0].id,
                reply_to_message_id=ReplyCheck(m),
            )
        except Exception as e:
            return await xx.edit("{} {}".format(em.gagal, e))
    else:
        await msg_id.copy(m.chat.id, reply_to_message_id=ReplyCheck(m))
    return await xx.delete()


async def get_raw_note(c, m, xx, note, data, msg_id):
    em = Emo(c)
    await em.init()
    await msg_id.copy(
        m.chat.id,
        reply_to_message_id=ReplyCheck(m),
        parse_mode=ParseMode.DISABLED,
    )
    return await xx.delete()


async def local_notes(client: ubot, message):
    emo = Emo(client)
    await emo.init()
    pros = await message.reply(
        f"<blockquote>{emo.proses} <b>Proses mengambil Daftar Catatan ..</b></blockquote>"
    )

    getnotes = monggo.all_var(client.me.id, "notes")

    if not getnotes:
        return await pros.edit(
            f"<blockquote>{emo.gagal} <b>Daftar catatan masih kosong.</b></blockquote>"
        )

    rply = "<b>❒ Berikut Daftar Catatan Anda:</b>\n┃\n"

    for count, (note_name, note_data) in enumerate(getnotes.items(), 1):
        note_type = note_data.get("type", "tidak diketahui")
        if count == len(getnotes):
            rply += f"┖ <code>{note_name}</code> | Tipe: {note_type}\n"
        else:
            rply += f"┣ <code>{note_name}</code> | Tipe: {note_type}\n"

    return await pros.edit(f"<blockquote>{rply}</blockquote>")


async def clear_note(client: ubot, message):
    emo = Emo(client)
    await emo.init()
    pros = await message.reply(
        f"<blockquote>{emo.proses} <b>Proses hapus catatan ..</b></blockquote>"
    )
    args = client.get_arg(message).split(",")
    gclog = monggo.get_log_group_id(client.me.id)
    logs = gclog if gclog else "me"
    if len(args) == 0 or (len(args) == 1 and args[0].strip() == ""):
        return await pros.edit(
            f"<blockquote>{emo.gagal} <b>Berikan nama catatan yang ingin anda hapus.</b></blockquote>"
        )
    gagal_list = []
    sukses_list = []
    for arg in args:
        arg = arg.strip()
        if not arg:
            continue
        data = monggo.get_var(client.me.id, arg, "notes")
        if not data:
            gagal_list.append(arg)
        else:
            monggo.remove_var(client.me.id, arg, "notes")
            await client.delete_messages(logs, int(data["message_id"]))
            sukses_list.append(arg)
    if sukses_list:
        return await pros.edit(
            f"<blockquote>{emo.sukses} <b><code>{', '.join(sukses_list)}</code> Berhadil dihapus.</b></blockquote>"
        )
    if gagal_list:
        return await pros.edit(
            f"<blockquote>{emo.gagal} <b>{', '.join(gagal_list)} Tidak ada dalam daftar Catatan.</b></blockquote>"
        )


async def inline_notes(client, iq):
    try:
        q = iq.query.split(None, 1)
        if len(q) < 2:
            return

        note = q[1]
        gw = iq.from_user.id
        noteval = monggo.get_var(gw, note, "notes")
        if not noteval:
            return

        item = [x for x in ubot._ubot if gw == x.me.id]
        gclog = monggo.get_log_group_id(gw)
        logs = gclog if gclog else "me"
        duar = []

        for me in item:
            msg = await me.get_messages(logs, int(noteval["message_id"]))
            tks = msg.caption if msg.caption else msg.text
            tg, nontg = cek_tautan(tks)

            if tg:
                note, button = get_msg_button(nontg)
                button = cb_nts_btn(gw, button) if button else None
                web_page = await get_media_type_from_url(me, tg)

                if web_page and web_page.video:
                    video_url = tg
                    thumb_url = tg

                    duar.append(
                        InlineQueryResultVideo(
                            video_url=video_url,
                            thumb_url=thumb_url,
                            title="note media!",
                            caption=note,
                            reply_markup=button,
                        )
                    )
                elif web_page and web_page.photo:
                    photo_url = tg
                    thumb_url = tg
                    duar.append(
                        InlineQueryResultPhoto(
                            photo_url=photo_url,
                            thumb_url=photo_url,
                            title="note media!",
                            caption=note,
                            reply_markup=button,
                        )
                    )
                else:
                    filem = (
                        InlineQueryResultVideo
                        if tg.endswith(".mp4")
                        else InlineQueryResultPhoto
                    )
                    if tg.endswith(".mp4"):
                        url_ling = {
                            "video_url": tg,
                            "thumb_url": tg,
                        }
                    elif tg.endswith(".jpg"):
                        url_ling = {
                            "photo_url": tg,
                        }
                    duar.append(
                        filem(
                            **url_ling,
                            title="note media!",
                            caption=note,
                            reply_markup=button,
                        )
                    )
            else:
                note, button = get_msg_button(tks)
                button = cb_nts_btn(gw, button) if button else None
                duar.append(
                    InlineQueryResultArticle(
                        title="note teks!",
                        input_message_content=InputTextMessageContent(
                            note, disable_web_page_preview=True
                        ),
                        reply_markup=button,
                    )
                )

        await client.answer_inline_query(iq.id, cache_time=0, results=duar)

    except Exception as e:
        await client.answer_inline_query(
            iq.id, cache_time=0, results=[], switch_pm_text=f"Kesalahan: {str(e)}"
        )


def remove_links(text: str) -> str:
    url_pattern = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
    return url_pattern.sub("", text)


async def cb_notes(c: bot, cq):
    ii = cq.data.split("_")
    cq.from_user
    try:
        notetag = ii[-2].replace("#", "")
        gw = ii[-1]
        item = [x for x in ubot._ubot if int(gw) == x.me.id]
        gclog = monggo.get_log_group_id(int(gw))
        logs = gclog if gclog else "me"
        noteval = monggo.get_var(int(gw), notetag, "notes")
        cekpic = monggo.get_var(int(gw), "PMPIC")
        costum_cq = cq.edit_message_caption if cekpic else cq.edit_message_text
        costum_text = "caption" if cekpic else "text"

        if not noteval:
            await cq.answer("Catatan tidak ditemukan.", True)
            return

        for me in item:
            msg = await me.get_messages(logs, int(noteval["message_id"]))

            if noteval["type"] in ["photo", "video"]:
                note, button = get_msg_button(msg.caption)
                button = cb_nts_btn(int(gw), button)
                note = remove_links(note)

                try:
                    await costum_cq(**{costum_text: note}, reply_markup=button)
                except FloodWait as e:
                    return await cq.answer(f"FloodWait {e}, Please Waiting!!", True)
            else:
                note, button = get_msg_button(msg.text)
                button = cb_nts_btn(int(gw), button)

                note = remove_links(note)

                try:
                    await costum_cq(**{costum_text: note}, reply_markup=button)
                except FloodWait as e:
                    return await cq.answer(f"FloodWait {e}, Please Waiting!!", True)

    except Exception as e:
        if any(err in str(e) for err in ["MESSAGE_NOT_MODIFIED", "PEER_ID_INVALID"]):
            pass