import asyncio
import os

from pyrogram.errors import *
from pyrogram.errors import FloodWait
from pyrogram.types import *

from ubot import *


scheduled_tasks = {}


__MODULE__ = "ꜱᴄʜᴇᴅᴜʟᴇ"
__HELP__ = """
ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀ ꜱᴄʜᴇᴅᴜʟᴇ

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ꜱᴅꜱᴘᴍ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴋᴇ ᴘᴇꜱᴀɴ]
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇᴍᴜʟᴀɪ ꜱᴄʜᴇᴅᴜʟᴇ ᴍᴇꜱꜱᴀɢᴇ ᴋᴇ ʟɪꜱᴛ ꜱᴄʜ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ꜱᴛᴅꜱᴘᴍ</ᴄᴏᴅᴇ>
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇᴍᴀᴛɪᴋᴀɴ ꜱᴄʜᴇᴅᴜʟᴇ ᴍᴇꜱꜱᴀɢᴇ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ʟɪꜱᴛꜱᴘᴍ</ᴄᴏᴅᴇ>
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇʟɪʜᴀᴛ ʟɪꜱᴛ ɢʀᴏᴜᴘ ʏᴀɴɢ ᴀᴅᴀ ᴅɪ ʟɪꜱᴛꜱᴄʜ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ᴀᴅᴅꜱᴘᴍ</ᴄᴏᴅᴇ>
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ɢʀᴏᴜᴘ ᴋᴇ ʟɪꜱᴛ ꜱᴄʜ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ᴅᴇʟꜱᴘᴍ</ᴄᴏᴅᴇ>
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇɴɢʜᴀᴘᴜꜱ ɢʀᴏᴜᴘ ᴅᴀʀɪ ʟɪꜱᴛ ꜱᴄʜ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ᴅᴇʟᴀʏꜱᴄʜ</ᴄᴏᴅᴇ> 
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇɴɢᴀᴛᴜʀ ᴡᴀᴋᴛᴜ ᴅᴇʟᴀʏ ꜱᴄʜ ᴅᴇꜰᴀᴜʟᴛ ɴʏᴀ ᴀᴅᴀʟᴀʜ 10 ᴅᴇᴛɪᴋ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ꜱᴀᴠᴇꜱᴄʜ</ᴄᴏᴅᴇ> [ɴᴀᴍᴀ ᴄᴀᴛᴀᴛᴀɴ ꜱᴄʜ]
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ꜱɪᴍᴘᴀɴ ᴛᴇᴋꜱ ꜱᴄʜᴇᴅᴜʟᴇ ᴍᴇꜱꜱᴀɢᴇ ᴋᴇ ᴅᴀᴛᴀʙᴀꜱᴇ ꜱᴄʜ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ɢᴇᴛꜱᴄʜ</ᴄᴏᴅᴇ> [ɴᴀᴍᴀ ᴄᴀᴛᴀᴛᴀɴ ꜱᴄʜ]
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇɴɢᴀᴍʙɪʟ ᴛᴇᴋꜱ ꜱᴄʜᴇᴅᴜʟᴇ ᴍᴇꜱꜱᴀɢᴇ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ʟɪꜱᴛꜱᴄʜ</ᴄᴏᴅᴇ>
⌑ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇʟɪʜᴀᴛ ʟɪꜱᴛ ᴄᴀᴛᴀᴛᴀɴ ꜱᴄʜ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ.

⌑ ᴄᴏᴍᴍᴀɴᴅ : <ᴄᴏᴅᴇ>{0}ᴄʟᴇᴀʀꜱᴄʜ</ᴄᴏᴅᴇ>
⌑ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : ᴍᴇɴɢʜᴀᴘᴜꜱ ᴄᴀᴛᴀᴛᴀɴ ꜱᴄʜ ᴅᴀʀɪ ʟɪꜱᴛ ᴅᴀᴛᴀʙᴀꜱᴇ.
"""

async def send_cmd(c: ubot, msgtype: int):
    GET_FORMAT = {
        Types.TEXT.value: c.send_message,
        Types.DOCUMENT.value: c.send_document,
        Types.PHOTO.value: c.send_photo,
        Types.VIDEO.value: c.send_video,
        Types.STICKER.value: c.send_sticker,
        Types.AUDIO.value: c.send_audio,
        Types.VOICE.value: c.send_voice,
        Types.VIDEO_NOTE.value: c.send_video_note,
        Types.ANIMATION.value: c.send_animation,
        Types.ANIMATED_STICKER.value: c.send_sticker,
        Types.CONTACT: c.send_contact,
    }
    return GET_FORMAT[msgtype]

@PY.UBOT("savesch")
async def _(c: ubot, m):
    em = Emo(c.me.id)
    em.initialize()
    gua = c.me.id
    cek = m.reply_to_message
    note_name, text, data_type, content = get_note_type(m)
    xx = await m.reply("{} Diproses...".format(em.proses))
    if not note_name:
        return await xx.edit("{} Silahkan berikan nama catatan {}".format(em.gagal, m.text))
    getnotes = monggo.get_text_sch(c.me.id, note_name)
    if getnotes:
        return await xx.edit("{} Notes already exist.".format(em.gagal))
    if data_type == Types.TEXT:
        monggo.save_text_sch(c.me.id, note_name, text, data_type, content)
    elif data_type in [Types.PHOTO, Types.VIDEO]:
        #file_type = "jpg" if data_type == Types.PHOTO else "mp4"
        #xo = kontol_siapa(gua, file_type)
        #mek = await c.download_media(cek, xo)
        #xo_url = upload_file(mek)
        #mmk = f"https://telegra.ph/{xo_url[0]}"
        monggo.save_text_sch(c.me.id, note_name, text, data_type, content)
        #os.remove(xo)
    elif data_type in [
        Types.STICKER,
        Types.VIDEO_NOTE,
        Types.ANIMATED_STICKER,
        Types.VOICE,
        Types.DOCUMENT,
        Types.AUDIO,
    ]:
        monggo.save_text_sch(c.me.id, note_name, text, data_type, content)
    
    await xx.edit("{} Catatan sch berhasil disimpan `{}`".format(em.sukses, note_name))
    return


@PY.UBOT("getsch")
async def _(c: ubot, m):
    em = Emo(c.me.id)
    em.initialize()
    xx = await m.reply("{} Diproses...".format(em.proses))
    note = None
    if len(m.text.split()) >= 2:
        note = m.text.split()[1]
    else:
        await xx.edit("{} Berikan nama catatan!!".format(em.gagal))
        return

    getnotes = monggo.get_text_sch(c.me.id, note)
    if not getnotes:
        return await xx.edit("{} Tidak ada catatan dengan nama {}".format(em.gagal, note))

    if getnotes["type"] == Types.TEXT:
        await m.reply(getnotes["value"])

    elif getnotes["type"] == Types.PHOTO:
        await c.send_photo(
            m.chat.id,
            getnotes["file"],
            caption=getnotes["value"],
            reply_to_message_id=ReplyCheck(m),
        )
    elif getnotes["type"] == Types.VIDEO:
        await c.send_video(
            m.chat.id,
            getnotes["file"],
            caption=getnotes["value"],
            reply_to_message_id=ReplyCheck(m),
        )
    elif getnotes["type"] == Types.STICKER:
        await c.send_sticker(
            m.chat.id, getnotes["file"], reply_to_message_id=ReplyCheck(m)
        )
    elif getnotes["type"] == Types.VOICE:
        await c.send_voice(
            m.chat.id,
            getnotes["file"],
            caption=getnotes["value"],
            reply_to_message_id=ReplyCheck(m),
        )
    elif getnotes["type"] == Types.VIDEO_NOTE:
        await c.send_video_note(
            m.chat.id,
            getnotes["file"],
            reply_to_message_id=ReplyCheck(m),
        )
    elif getnotes["type"] == Types.ANIMATED_STICKER:
        await c.send_sticker(
            m.chat.id,
            getnotes["file"],
            reply_to_message_id=ReplyCheck(m),
        )
    else:
        await c.send_media_group(
            m.chat.id,
            getnotes["file"],
            reply_to_message_id=ReplyCheck(m),
        )
    await xx.delete()
    return


@PY.UBOT("listsch")
async def _(c: ubot, m):
    em = Emo(c.me.id)
    em.initialize()
    xx = await m.reply("{} Diproses...".format(em.gagal))
    getnotes = monggo.get_all_text_schs(c.me.id)
    if not getnotes:
        await xx.edit("{} Tidak ada catatan satupun!!".format(em.gagal))
        return
    rply = "{} Daftar catatan schedule:\n\n".format(em.sukses)
    for x in getnotes:
        if len(rply) >= 1800:
            await xx.edit(rply)
        rply += "• {}\n".format(x)

    await xx.edit(rply)
    return


@PY.UBOT("clearsch")
async def _(c: ubot, m):
    em = Emo(c.me.id)
    em.initialize()
    xx = await m.reply("{} Diproses...".format(em.gagal))
    if len(m.text.split()) <= 1:
        return await xx.edit("{} Berikan nama catatan untuk dihapus!!".format(em.gagal))

    note = m.text.split()[1]
    getnotes = monggo.get_all_text_schs(c.me.id)
    rmnot = monggo.rm_text_sch(c.me.id, note)

    if note not in getnotes and not rmnot:
        await xx.edit("{} Catatan {} tidak ditemukan".format(em.gagal, note))
        return
    else:
        await xx.edit("{} Catatan {} berhasil dihapus!!".format(em.sukses, note))
        return


@PY.UBOT("sdspm")
async def _(c, m):
    em = Emo(c.me.id)
    em.initialize()
    if len(m.command) < 2:
        return await m.reply("Berikan nama teks spam yang ingin dikirim.")

    cekdele = monggo.get_var(c.me.id, "delayspam")
    if cekdele:
        interval = int(cekdele)
    else:
        interval = 10
    ambil_sch_name = m.text.split()[1]
    diget_value = monggo.get_text_sch(c.me.id, ambil_sch_name)
    if not diget_value:
        return await m.reply("{} **Catatan `{}` tidak ditemukan!**".format(em.gagal, ambil_sch_name))
    yoki = await send_cmd(c, diget_value["type"])
    scheduled_message = None
    if diget_value["type"] == Types.TEXT:
        scheduled_message = f"{diget_value['value']}"

    elif diget_value["type"] in [Types.PHOTO, Types.VIDEO, Types.VOICE]:
        scheduled_message = f"{diget_value['file']}"
        scheduled_cap = f"{diget_value['value']}"
        
    elif diget_value["type"] in [Types.STICKER,Types.VIDEO_NOTE,Types.ANIMATED_STICKER]:
        scheduled_message = f"{diget_value['file']}"
    else:
        scheduled_message = f"{diget_value['file']}"
    
    chat_ids = monggo.list_sch(c.me.id)
    for chat_id in chat_ids:

        async def send_scheduled_message(chat_id):
            try:
                while True:
                    if diget_value["type"] == Types.TEXT:
                        await asyncio.sleep(interval)
                        await c.send_message(chat_id, scheduled_message)
                    elif diget_value["type"] in [Types.STICKER,Types.VIDEO_NOTE,Types.ANIMATED_STICKER,Types.VOICE,Types.DOCUMENT,Types.AUDIO]:
                        await asyncio.sleep(interval)
                        await yoki(chat_id, scheduled_message)
                    else:
                        await asyncio.sleep(interval)
                        await yoki(chat_id,scheduled_message,caption=scheduled_cap)
            except ChatWriteForbidden:
                pass
            except SlowmodeWait as e:
                  await asyncio.sleep(e.value)
                  task = asyncio.create_task(send_scheduled_message(chat_id))
                  scheduled_tasks[chat_id] = task
            except UserBannedInChannel:
                  return await m.reply("Gagal memulai schedule karna akun anda dibatasi!!")
                  
            except FloodWait as e:
                await asyncio.sleep(e.value)
                task = asyncio.create_task(send_scheduled_message(chat_id))
                scheduled_tasks[chat_id] = task

        task = asyncio.create_task(send_scheduled_message(chat_id))
        scheduled_tasks[chat_id] = task
    await m.reply(f"Done.")
    return


@PY.UBOT("stdspm")
async def _(c, m):
    chat_ids = monggo.list_sch(c.me.id)
    for chat_id in chat_ids:
        if chat_id in scheduled_tasks:
            task = scheduled_tasks[chat_id]
            task.cancel()
            del scheduled_tasks[chat_id]
    await m.reply("Stopped.")
    return


@PY.UBOT("listspm")
async def _(c, m):
    teks = "Daftar Schaduled:\n\n"
    user_id = c.me.id
    lists = monggo.list_sch(user_id)
    if len(lists) == 0:
        await m.reply("Database kosong.")
        return
    else:
        for count, chat_id in enumerate(lists, 1):
            teks += f"{count}. `{chat_id}`\n"
        await m.reply(teks)
        return


@PY.UBOT("delaysch")
async def _(c, m):
    rr = get_arg(m)
    if not rr:
        return await m.reply("Berikan angka delay sch.")
    if not rr.isnumeric():
        return await m.reply("Masukkan angka.")
    monggo.set_var(c.me.id, "delayspam", rr)
    return await m.reply(f"Delay diatur ke {rr}")


@PY.UBOT("addspm|delspm")
async def _(c, m):
    if m.command[0] == "addspm":
        user_id = c.me.id
        if len(m.command) == 1:
            chat_id = m.chat.id
        else:
            chat_id = int(m.command[1])
        monggo.add_sch(user_id, chat_id)
        return await m.reply(f"{chat_id} Berhasil di tambahkan.")
    elif m.command[0] == "delspm":
        user_id = c.me.id
        if len(m.command) == 1:
            chat_id = m.chat.id
        else:
            chat_id = int(m.command[1])
        monggo.del_sch(user_id, chat_id)
        return await m.reply(f"{chat_id} Berhasil di hapus.")
