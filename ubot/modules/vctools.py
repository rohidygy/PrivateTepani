__MODULE__ = "ᴠᴄᴛᴏᴏʟꜱ"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ 』</b>

⌑ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}startvc</code>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}stopvc</code>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}jvc</code>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ʙᴇʀɢᴀʙᴜɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <code>{0}lvc</code>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.
"""


from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from pytgcalls.exceptions import AlreadyJoinedError

from ubot import *

async def get_group_call(

    client: Client, message: Message, err_msg: str = ""

) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"<b>No group call Found</b> {err_msg}")
    return False

@PY.UBOT("jvc")
async def joinvc(client, message):
    pros = await message.reply(
        f"<blockquote>{emo.proses} <b>Proses bergabung ke obrolan suara ..</b></blockquote>"
    )

    chat = message.command[1] if len(message.command) > 1 else message.chat.id

    try:
        if isinstance(chat, int):
            chat_id = chat
        else:
            chat_info = await client.get_chat(chat)
            chat_id = chat_info.id

        try:
            info = await client.get_chat(chat_id)
            title = info.title if info.title else f"{chat_id}"
        except:
            title = f"{chat_id}"

        try:
            await client.call_py.play(chat_id)
            await client.call_py.mute_stream(chat_id)
            await pros.edit(
                f"<blockquote>{emo.sukses} <b>Berhasil Bergabung ke Obrolan suara:\n{emo.profil} Chat : <code>{title}</code></b></blockquote>"
            )
        except AlreadyJoinedError:
            await pros.edit(
                f"<blockquote>{emo.gagal} <b>Akun anda sudah Bergabung sebelumnya.</b></blockquote>"
            )
        except Exception as e:
            await pros.edit(
                f"<blockquote>{emo.gagal} <b>Error:</b>\n<code>{e}</code></blockquote>"
            )
    except Exception as e:
        await pros.edit(
            f"<blockquote>{emo.gagal} <b>Error:</b>\n<code>{e}</code></blockquote>"
        )


@PY.UBOT("lvc")
async def leavevc(client, message):
    pros = await message.reply(
        f"<blockquote>{emo.proses} <b>Proses meninggalkan obrolan suara ..</b></blockquote>"
    )

    chat = message.command[1] if len(message.command) > 1 else message.chat.id

    try:
        if isinstance(chat, int):
            chat_id = chat
        else:
            chat_info = await client.get_chat(chat)
            chat_id = chat_info.id

        try:
            info = await client.get_chat(chat_id)
            title = info.title if info.title else f"{chat_id}"
        except:
            title = f"{chat_id}"

        try:
            await client.call_py.leave_call(chat_id)
            await pros.edit(
                f"<blockquote>{emo.sukses} <b>Berhasil Meninggalkan Obrolan Suara.\n{emo.profil} Chat : <code>{title}</code></b></blockquote>"
            )
        except Exception as e:
            await pros.edit(
                f"<blockquote>{emo.gagal} <b>Error:</b>\n<code>{e}</code></blockquote>"
            )
    except Exception as e:
        await pros.edit(
            f"<blockquote>{emo.gagal} <b>Error:</b>\n<code>{e}</code></blockquote>"
        )


@PY.UBOT("startvc")
async def opengc(client: Client, message: Message):
    ky = await eor(message, "`Processing....`")
    vctitle = get_arg(message)
    if message.chat.type == "channel":
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"<b>Active Voice Chat</b>\n • <b>Chat</b> : {message.chat.title}"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title:</b> {vctitle}"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")

@PY.UBOT("stopvc")
async def end_vc_(client: Client, message: Message):
    ky = await eor(message, f"<emoji id=6010111371251815589>⏳</emoji> `Processing....`")
    if not (group_call := await get_group_call(client, message, err_msg=", Error...")):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(f"<b>Voice Chat Ended</b>\n • <b>Chat</b> : {message.chat.title}")
