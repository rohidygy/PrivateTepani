from ubot import *

__MODULE__ = "Group"
__HELP__ = """
 Bantuan Untuk Group

• Perintah : <code>{0}zombies</code>
• Penjelasan : Untuk mencari akun terhapus dalam grup kemudian mengeluarkan nya.(admin required)

• Perintah : <code>{0}pin</code> or <code>{0}upin</code> [reply message]
• Penjelasan : Untuk menyematkan dan melepas sematan.

• Perintah : <code>{0}getlink</code>
• Penjelasan : Untuk mengambil tautan link grup (admin required)

• Perintah : <code>{0}promote</code> [user_id/username/reply user]
• Penjelasan : Untuk mengangkatkan anggota menjadi admin di grup dengan izin terbatas.

• Perintah : <code>{0}fullpromote</code> [user_id/username/reply user]
• Penjelasan : Untuk mengangkatk anggota menjadi admin di grup dengan izin wakil pendiri.

• Perintah : <code>{0}demote</code> [user_id/username/reply user]
• Penjelasan : Untuk menurunkan anggota dari admin grup.

• Perintah : <code>gctitle</code> [teks or reply teks]
• Penjelasan : Untuk mengubah nama grup.

• Perintah : <code>gcdes</code> [teks or reply teks]
• Penjelasan : Untuk mengubah nama deskripsi grup.

• Perintah : <code>gcpic</code> [reply photo or videl]
• Penjelasan : Untuk mengubah foto grup.
"""

@PY.UBOT("pin|unpin", sudo=True)
async def _(client, message):
    await pin_message(client, message)


@PY.UBOT("promote|fullpromote", sudo=True)
async def _(client, message):
    await promotte(client, message)


@PY.UBOT("demote", sudo=True)
async def _(client, message):
    await demote(client, message)


@PY.UBOT("getlink", sudo=True)
async def _(client, message):
    await invite_link(client, message)
    
    
@PY.UBOT("zombies")
async def _(c, m):
    em = Emo(c.me.id)
    em.initialize()
    chat_id = m.chat.id
    deleted_users = []
    banned_users = 0
    m = await m.reply("{} Diproses...".format(em.proses))

    async for i in c.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                await m.chat.ban_member(deleted_user)
            except Exception:
                pass
            banned_users += 1
        await m.edit("{} **Berhasil mengeluarkan `{}` akun terhapus.**".format(em.sukses, banned_users))
        return
    else:
        await m.edit("{} **Tidak ada akun terhapus disini!**".format(em.gagal))
        return
      
      
@PY.UBOT("gctitle")
async def _(c, m):
    em = Emo(c.me.id)
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text("{} Berikan judul".format(em.gagal))
        return
    if m.reply_to_message:
        gtit = m.reply_to_message.text
    else:
        gtit = m.text.split(None, 1)[1]
    try:
        await m.chat.set_title(gtit)
    except Exception as e:
        return await m.reply_text("{} Error {}".format(em.gagal, e))
    return await m.reply_text("{} Judul Grup berhasil diubah menjadi : {}".format(em.sukses, gtit))


@PY.UBOT("gcdes")
async def _(c, m):
    em = Emo(c.me.id)
    em.initialize()
    if len(m.text.split()) == 1 and not m.reply_to_message:
        await m.reply_text("{} **Silahkan balas ke pesan atau berikan pesan.**".format(em.gagal))
        return
    if m.reply_to_message:
        desp = m.reply_to_message.text
    else:
        desp = m.text.split(None, 1)[1]
    try:
        await m.chat.set_description(desp)
    except Exception as e:
        return await m.reply_text("{} Error {}".format(em.gagal, e))
    return await m.reply_text("{} **Berhasil mengubah deskripsi Grup : {} menjadi {}.**".format(em.sukses, m.chat.description, desp))
    
    
@PY.UBOT("gcpic")
async def _(c, m):
    em = Emo(c.me.id)
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text("{} Silahkan balas ke media!!".format(em.gagal))
    if (
        not m.reply_to_message.photo
        and not m.reply_to_message.document
        and not m.reply_to_message.video
    ):
        return await m.reply_text("{} Balas ke media foto atau video!!".format(em.gagal))

    if m.reply_to_message:
        if m.reply_to_message.photo:
            await c.set_chat_photo(m.chat.id, photo=m.reply_to_message.photo.file_id)
            await m.reply_text("{} Berhasil diatur menjadi foto grup.".format(em.sukses))
        if m.reply_to_message.document:
            await c.set_chat_photo(m.chat.id, photo=m.reply_to_message.document.file_id)
            await m.reply_text("{} Berhasil diatur menjadi foto grup.".format(em.sukses))
        elif m.reply_to_message.video:
            await c.set_chat_photo(m.chat.id, video=m.reply_to_message.video.file_id)
            await m.reply_text("{} Berhasil diatur menjadi foto grup.".format(em.sukses))
    else:
        return await m.reply_text("{} Balas ke media foto atau video!!".format(em.gagal))