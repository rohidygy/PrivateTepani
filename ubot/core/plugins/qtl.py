import asyncio
import os

from pyrogram.raw.functions.messages import DeleteHistory


async def quotly_cmd(client, message):
    info = await message.reply("<b>Processing...</b>")
    await client.unblock_user("@QuotLyBot")
    if message.reply_to_message:
        if len(message.command) < 2:
            msg = [message.reply_to_message]
        else:
            try:
                count = int(message.command[1])
            except Exception as error:
                await info.edit(error)
            msg = [
                i
                for i in await client.get_messages(
                    chat_id=message.chat.id,
                    message_ids=range(
                        message.reply_to_message.id, message.reply_to_message.id + count
                    ),
                    replies=-1,
                )
            ]
        try:
            for x in msg:
                await x.forward("@QuotLyBot")
        except Exception:
            pass
        await asyncio.sleep(9)
        await info.delete()
        async for quotly in client.get_chat_history("@QuotLyBot", limit=1):
            if not quotly.sticker:
                await message.reply(f"❌ @QuotLyBot Error")
            else:
                sticker = await client.download_media(quotly)
                await message.reply_sticker(sticker)
                os.remove(sticker)
    else:
        if len(message.command) < 2:
            return await info.edit("<code>Balas ke pesan</code>")
        else:
            msg = await client.send_message(
                "@QuotLyBot", f"/qcolor {message.command[1]}"
            )
            await asyncio.sleep(1)
            get = await client.get_messages("@QuotLyBot", msg.id + 1)
            await info.edit(
                f"<b>Warna latar belakang di ganti ke :</b> <code>{get.text.split(':')[1]}</code>"
            )
    user_info = await client.resolve_peer("@QuotLyBot")
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
