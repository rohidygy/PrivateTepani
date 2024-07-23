from asyncio import sleep

from pyrogram import *
from pyrogram.types import *

from ubot import FKM, PY, Emo, monggo, ubot

__MODULE__ = "Settings"
__HELP__ = """
Bantuan Untuk Settings

• Perintah: <code>{0}setprefix</code> [trigger]
• Penjelasan: Untuk mengatur handler userbot anda.

• Perintah: <code>{0}setvar</code> [variable] [value]
• Penjelasan: Untuk mengubah tampilan emoji.

• Perintah: <code>{0}emoid</code> [reply emoji]
• Penjelasan: Untuk mengubah tampilan emoji.

• Perintah: <code>{0}getemo</code>
• Penjelasan: Untuk melihat tampilan emoji.

• Perintah: <code>{0}getvar</code>
• Penjelasan: Untuk melihat variabel dan value anda.

• Contoh pengunaan set emoji dan setprefix :

<code>{0}setvar ping 🏓</code>
<code>{0}setvar pong 🥵</code>
<code>{0}setvar proses 🔄</code>
<code>{0}setvar sukses ✅</code>
<code>{0}setvar gagal ❌</code>
<code>{0}setvar profil 👤</code>
<code>{0}setvar alive ⭐</code>

<code>{0}setprefix 1 - ( + ) none</code>

Untuk akun premium bisa menggunakan emoji premium.
"""


@PY.DEP("Absen")
async def _(client, message):
    await message.reply("<b>Mmuuaahh😘</b>")

@PY.DEP("cekbot")
async def _(client, message):
    await message.reply("<b>Aktif Bosque😘</b>")

@PY.DEP("batu")
async def _(client, message):
    await client.send_reaction(message.chat.id, message.id, "🗿")


@PY.UBOT("setprefix", sudo=True)
async def _(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    Tm = await message.reply(f"{emo.proses} <b>Processing...</b>")
    await sleep(2)
    if len(message.command) < 2:
        return await Tm.edit(f"{emo.gagal} <b>Prefix harus berupa trigger.</b>")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(client.me.id, ub_prefix)
            monggo.set_pref(client.me.id, ub_prefix)
            parsed_prefix = " ".join(f"{prefix}" for prefix in ub_prefix)
            return await Tm.edit(
                f"{emo.sukses} <b>Prefix diatur ke : <code>{parsed_prefix}</code></b>"
            )
        except Exception as error:
            await Tm.edit(str(error))


@PY.UBOT("emoid", sudo=True)
async def emoid(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    Tm = await message.edit(f"{emo.proses} <b>Processing...</b>")
    emoji = message.reply_to_message
    if emoji.entities:
        for entot in emoji.entities:
            if entot.custom_emoji_id:
                emoid = entot.custom_emoji_id
                await Tm.edit(
                    f"{emo.sukses} <b>Custom Emoji ID : <code>{emoid}</code>.</b>"
                )
            else:
                await Tm.edit(f"{emo.gagal} <b>Reply ke Custom Emoji.</b>")


@PY.UBOT("setvar", sudo=True)
@ubot.on_message(filters.user(FKM) & filters.command("setvar", "") & ~filters.me)
async def set_emoji(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    gua = client.me.is_premium
    jing = await message.reply(f"{emo.proses} <b>Processing...</b>")
    if len(message.command) < 3:
        return await jing.edit(
            f"{emo.gagal} <b>Gunakan Format : <code>setvar variable value</code>.</b>"
        )
    command, variable, value = message.command[:3]
    emoji_id = None
    if variable.lower() == "ping":
        if gua == True:
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    monggo.set_var(client.me.id, "emo_ping", emoji_id)
                    await jing.edit(
                        f"{emo.sukses} <b>Emoji ping diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            monggo.set_var(client.me.id, "emo_ping", value)
            await jing.edit(f"{emo.sukses} <b>Emoji ping diset ke :</b> {value}")
    elif variable.lower() == "pong":
        if gua == True:
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    monggo.set_var(client.me.id, "emo_pong", emoji_id)
                    await jing.edit(
                        f"{emo.sukses} <b>Emoji pong diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            monggo.set_var(client.me.id, "emo_pong", value)
            await jing.edit(f"{emo.sukses} <b>Emoji pong diset ke :</b> {value}")
    elif variable.lower() == "proses":
        if gua == True:
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    monggo.set_var(client.me.id, "emo_proses", emoji_id)
                    await jing.edit(
                        f"{emo.sukses} <b>Emoji proses diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            monggo.set_var(client.me.id, "emo_proses", value)
            await jing.edit(f"{emo.sukses} <b>Emoji proses diset ke :</b> {value}")
    elif variable.lower() == "gagal":
        if gua == True:
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    monggo.set_var(client.me.id, "emo_gagal", emoji_id)
                    await jing.edit(
                        f"{emo.sukses} <b>Emoji gagal diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            monggo.set_var(client.me.id, "emo_gagal", value)
            await jing.edit(f"{emo.sukses} <b>Emoji gagal diset ke :</b> {value}")
    elif variable.lower() == "sukses":
        if gua == True:
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                   monggo.set_var(client.me.id, "emo_owner", emoji_id)
                await jing.edit(
                        f"{emo.sukses} <b>Emoji owner diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            monggo.set_var(client.me.id, "emo_owner", value)
            await jing.edit(f"{emo.sukses} <b>Emoji pong diset ke :</b> {value}")
    elif variable.lower() == "proses":
        if gua == True:
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                   if emoji_id:
                    monggo.set_var(client.me.id, "emo_sukses", emoji_id)
                    await jing.edit(
                        f"{emo.sukses} <b>Emoji sukses diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            monggo.set_var(client.me.id, "emo_sukses", value)
            await jing.edit(f"{emo.sukses} <b>Emoji sukses diset ke :</b> {value}")
    elif variable.lower() == "profil":
        if gua == True:
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    monggo.set_var(client.me.id, "emo_profil", emoji_id)
                    await jing.edit(
                        f"{emo.sukses} <b>Emoji profil diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            monggo.set_var(client.me.id, "emo_profil", value)
            await jing.edit(f"{emo.sukses} <b>Emoji profil diset ke :</b> {value}")
    elif variable.lower() == "alive":
        if gua == True:
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break
                if emoji_id:
                    monggo.set_var(client.me.id, "emo_alive", emoji_id)
                    await jing.edit(
                        f"{emo.sukses} <b>Emoji profil diset ke :</b> <emoji id={emoji_id}>{value}</emoji>"
                    )
        elif gua == False:
            monggo.set_var(client.me.id, "emo_alive", value)
            await jing.edit(f"{emo.sukses} <b>Emoji profil diset ke :</b> {value}")
    elif variable.lower() == "antipm":
        if value.lower() == "off":
            monggo.remove_var(client.me.id, "ANTI_PM")
            await jing.edit(f"{emo.sukses} <b>AntiPM Dimatikan.</b>")
        else:
            monggo.set_var(client.me.id, "ANTI_PM", True)
            await jing.edit(f"{emo.sukses} <b>AntiPM Dihidupkan.</b>")
    elif variable.lower() == "pmpic":
        if value.lower() == "off":
            monggo.remove_var(client.me.id, "PM_PIC")
            await jing.edit(f"{emo.sukses} <b>PM PIC Dimatikan.</b>")
        else:
            monggo.set_var(client.me.id, "PM_PIC", value)
            await jing.edit(
                f"{emo.sukses} <b>PM PIC Diatur ke : <code>{value}<code>.</b>"
            )
    elif variable.lower() == "pmtext":
        if value.lower() == "clear":
            monggo.remove_var(client.me.id, "PM_TEXT")
            await jing.edit(f"{emo.sukses} <b>PM TEXT Diatur ke Default.</b>")
    else:
        await jing.edit(
            f"{emo.gagal} <b>Silakan ketik <code>help {message.text}<code>.</b>"
        )


@PY.UBOT("getemo", sudo=True)
async def getemoji(client, message):
    emo = Emo(client.me.id)
    emo.initialize()
    xx = await message.reply(f"{emo.proses} <b>Processing...</b>")
    await xx.edit(
        f"{emo.sukses} <b>๏ Emoji kamu :</b>\n\n PING : {emo.ping}\n PONG : {emo.pong}\n PROSES : {emo.proses}\n SUKSES : {emo.sukses}\n GAGAL : {emo.gagal}\n PROFIL : {emo.profil}\n ALIVE : {emo.alive}"
    )
