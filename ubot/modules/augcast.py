import asyncio
import random

from pyrogram.errors import (ChatWriteForbidden, FloodWait, PeerIdInvalid,
                             SlowmodeWait)

from ubot import BLACKLIST_CHAT, PY, font, gen_font, get_broadcast_id, monggo

spam_gikesan = {}

__MODULE__ = "Auto Gcast"
__HELP__ = """
 Bantuan Untuk Auto Gcast

• Perintah : <code>{0}addkata</code> [Balas ke pesan]
• Penjelasan : Tambah kata gikes .

• Perintah : <code>{0}remkata</code> [Kasih Teks]
• Penjelasan : Apus kata gikes.

• Perintah : <code>{0}bgcdb</code> 
• Penjelasan : Gas random gikes.

• Perintah : <code>{0}cekkata</code> 
• Penjelasan : Cek kata gikes

• Perintah : <code>{0}sgcdb</code> 
• Penjelasan : Matiin spam gikes random.
"""


async def spam_kontol_gikes_memek(client, gc, kata_list, kirim_kata, index_gikes):
    try:
        while True:
            for _ in range(10):
                await asyncio.sleep(10)
                try:
                    katanya = index_gikes % len(kata_list)
                    xx = kata_list[katanya]
                    pili_kondom = random.choice(list(font.values()))
                    fnt = gen_font(xx, pili_kondom)
                    kata = f"<b>{fnt}</b>"
                    await client.send_message(gc, kata)
                    index_gikes += 1
                    kirim_kata.append(katanya)
                except (PeerIdInvalid, ChatWriteForbidden, SlowmodeWait):
                    continue

            await asyncio.sleep(300)

    except FloodWait:
        if gc in spam_gikesan:
            task = spam_gikesan[gc]
            task.cancel()
            del spam_gikesan[gc]


@PY.UBOT("bgcdb", sudo=True)
async def _(client, message):
    await message.reply(f"<b>Ok Diproses, kalo mo matiin ketik `sgcdb`.</b>")
    cek_gc = await get_broadcast_id(client, "group")
    blacklist = monggo.get_chat(client.me.id)
    ambil_bang = monggo.ambil_daftar(client.me.id)

    for gc in cek_gc:
        if gc in blacklist or gc in BLACKLIST_CHAT:
            continue

        try:
            kirim_kata = []
            index_gikes = 0

            task = asyncio.create_task(
                spam_kontol_gikes_memek(
                    client,
                    gc,
                    ambil_bang,
                    kirim_kata,
                    index_gikes,
                )
            )
            spam_gikesan[gc] = task
        except Exception as e:
            print(e)


@PY.UBOT("addkata", sudo=True)
async def _(client, message):
    if message.reply_to_message:
        kata = message.reply_to_message.text
    else:
        kata = message.text.split(None, 1)[1]
    if not kata:
        return await message.reply_text("<b>Minimal kasih teks lah anj</b>")
    monggo.tambah_kata(client.me.id, kata)
    await message.reply_text(f"<b>Masuk <code>{kata}</code> ke kata gikes.</b>")


@PY.UBOT("remkata", sudo=True)
async def _(client, message):
    if message.reply_to_message:
        kata = message.reply_to_message.text
    else:
        kata = message.text.split(None, 1)[1]
    if not kata:
        return await message.reply_text("<b>Minimal kasih teks lah anj</b>")
    monggo.kureng_kata(client.me.id, kata)
    await message.reply_text(f"<b>Dihapus <code>{kata}</code> dari kata gikes.</b>")


@PY.UBOT("cekkata", sudo=True)
async def _(client, message):
    gua = await client.get_me()
    data = monggo.ambil_daftar(client.me.id)
    if not data:
        await message.reply_text("<b>Kosong kintl kata gikesnya</b>")
    else:
        msg = f"Nih kata kata gikes jamet lu <code>{gua.first_name}</code> :\n"
        for kata in data:
            msg += f"<b>-</b> <code>{kata}</code>\n"
        await message.reply_text(msg)


@PY.UBOT("sgcdb", sudo=True)
async def _(client, message):
    cek_gc = await get_broadcast_id(client, "group")
    for chat_id in cek_gc:
        if chat_id in spam_gikesan:
            task = spam_gikesan[chat_id]
            task.cancel()
            del spam_gikesan[chat_id]
    await message.reply("<b>Oke jing berenti.</b>")
