import asyncio
from pyrogram.errors import *
dispam = []

berenti = False


async def spam_cmd(client, message):
    global berenti

    reply = message.reply_to_message
    msg = await message.reply("Processing...")
    berenti = True

    if reply:
        try:
            count_message = int(message.command[1])
            for i in range(count_message):
                if not berenti:
                    break
                await reply.copy(message.chat.id)
                await asyncio.sleep(0.1)
        except SlowmodeWait:
            pass
        except ChatWriteForbidden:
            pass
        except Exception as error:
            return await msg.edit(str(error))
        # berenti = False
    else:
        if len(message.command) < 2:
            return await msg.edit(
                f"Silakan ketik <code>{message.command}</code> untuk bantuan perintah."
            )
        else:
            try:
                count_message = int(message.command[1])
                for i in range(count_message):
                    if not berenti:
                        break
                    await message.reply(message.text.split(None, 2)[2])
                    await asyncio.sleep(0.1)
            except SlowmodeWait:
                pass
            except ChatWriteForbidden:
                pass
            except Exception as error:
                return await msg.edit(str(error))
    berenti = False

    await msg.delete()
    await message.delete()


async def dspam_cmd(client, message):
    global berenti

    reply = message.reply_to_message
    msg = await message.reply("Processing...")
    berenti = True
    if reply:
        try:
            count_message = int(message.command[1])
            count_delay = int(message.command[2])
        except Exception as error:
            return await msg.edit(str(error))
        for i in range(count_message):
            if not berenti:
                break
            try:
                await reply.copy(message.chat.id)
                await asyncio.sleep(count_delay)
            except:
                pass
    else:
        if len(message.command) < 4:
            return await msg.edit(
                f"Silakan ketik <code>{message.command}</code> untuk bantuan perintah."
            )
        else:
            try:
                count_message = int(message.command[1])
                count_delay = int(message.command[2])
            except Exception as error:
                return await msg.edit(str(error))
            for i in range(count_message):
                if not berenti:
                    break
                try:
                    await message.reply(message.text.split(None, 3)[3])
                    await asyncio.sleep(count_delay)
                except:
                    pass

    berenti = False

    await msg.delete()
    await message.delete()


async def capek_dah(client, message):
    global berenti

    # anu = await message.reply("Processing...")
    if not berenti:
        return await message.reply("Sedang tidak ada perintah spam disini.")
    berenti = False
    # dispam.remove(message.chat.id)
    await message.reply("Ok spam berhasil dihentikan.")

async def dspam_fwd(c, message):
    global berenti
    message.reply_to_message
    proses = await message.reply("Diproses....")
    berenti = True

    try:
        _, count_str, delay_str, link = message.text.split(maxsplit=3)
        count = int(count_str)
        delay = int(delay_str)
    except ValueError:
        await proses.reply(f"**Gunakan format :`{message.text}` [jumlah] [waktu delay] [link].**")
        await proses.delete()
        return

    chat_id, message_id = link.split("/")[-2:]

    try:
        chat_id = int(chat_id)
    except ValueError:
        pass

    message_id = int(message_id)

    for _ in range(count):
        try:
            if not berenti:
                break
            await c.get_messages(chat_id, message_id)
            await c.forward_messages(message.chat.id, chat_id, message_ids=message_id)
            await proses.delete()
            await message.delete()
            await asyncio.sleep(delay)
        except Exception as e:
            if (
                "CHAT_SEND_PHOTOS_FORBIDDEN" in str(e)
                or "CHAT_SEND_MEDIA_FORBIDDEN" in str(e)
                or "USER_RESTRICTED" in str(e)
            ):
                await message.reply("Dilarang digrup ini!!")
                await proses.delete()
            else:
                await proses.reply("Error!!")
                await proses.delete()
            break
    berenti = False
    await message.delete()
    await proses.delete()
    return