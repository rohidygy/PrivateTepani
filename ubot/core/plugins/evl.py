import asyncio
import os
import platform
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from os import execvp
from subprocess import PIPE, Popen, TimeoutExpired
from sys import executable
from time import perf_counter

import psutil

from ubot import *


async def restart():
    execvp(executable, [executable, "-m", "ubot"])


async def ngapdate(c, m):
    await m.delete()
    os.system("git pull")
    await restart()


async def liat_berapa(c, m):
    tt = await m.reply("Bentar diliat...")
    xx = len(ubot._ubot)
    await tt.edit(f"Jumlah Babi Liar Ada : {xx}")


async def shell_cmd(c, m):
    if len(m.command) < 2:
        return await m.reply("Input text!")
    cmd_text = m.text.split(maxsplit=1)[1]
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "bot#" if os.getuid() == 0 else "bot$"
    text = f"{char} <code>{cmd_text}</code>\n\n"

    try:
        perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "Timeout expired!"
    else:
        perf_counter()
        if len(stdout) > 4096:
            anuk = await m.reply("Oversize, sending file...")
            file = open("output.txt", "w+")
            file.write(stdout)
            file.close()
            await c.send_document(
                m.chat.id,
                "output.txt",
                reply_to_message_id=m.id,
            )
            await anuk.delete()
            os.remove("output.txt")
        else:
            text += f"<pre>{stdout}</pre>"
        if stderr:
            text += f"<pre>{stderr}</pre>"
    await m.reply(text)
    cmd_obj.kill()


async def evalator_cmd(c, m):
    if not get_arg(m):
        return
    TM = await m.reply_text("Processing ...")
    cmd = m.text.split(" ", maxsplit=1)[1]
    reply_to_ = m.reply_to_message or m
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await ubot.aexec(cmd, c, m)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "<b>OUTPUT</b>:\n"
    final_output += f"<pre>{evaluation.strip()}</pre>"
    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output)
    await TM.delete()


async def trash_cmd(c, m):
    if m.reply_to_message:
        msg_id = m.reply_to_message.id
    else:
        msg_id = m.id
    try:
        msgs = await c.get_messages(m.chat.id, msg_id)
        if len(str(msgs)) > 4096:
            with BytesIO(str.encode(str(msgs))) as out_file:
                out_file.name = "trash.txt"
                return await m.reply_document(document=out_file)
        else:
            return await m.reply(msgs)
    except Exception as error:
        return await m.reply(str(error))


async def get_my_otp(c, m):
    TM = await m.reply("<b>sᴇᴅᴀɴɢ Processing...</b>")
    if len(m.command) < 2:
        return await TM.edit("<b>ᴘᴀʏᴀʜ ɢɪᴛᴜ ᴀᴊᴀ ɴɢɢᴀᴋ ʙɪsᴀ</b>")
    else:
        for X in ubot._ubot:
            if int(m.command[1]) == X.me.id:
                if m.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if not otp.text:
                            await m.reply(
                                "<b>❌ ᴋᴏᴅᴇ ᴏᴛᴘ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>", quote=True
                            )
                        else:
                            await m.reply(otp.text)
                            await X.delete_messages(X.me.id, otp.id)
                    await TM.delete()
                else:
                    return await TM.edit(X.me.phone_number)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


async def vps(client, callback_query):
    uname = platform.uname()
    softw = "Informasi Sistem\n"
    softw += f"Sistem   : {uname.system}\n"
    softw += f"Rilis    : {uname.release}\n"
    softw += f"Versi    : {uname.version}\n"
    softw += f"Mesin    : {uname.machine}\n"

    boot_time_timestamp = psutil.boot_time()

    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"Waktu Hidup: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}\n"

    softw += "\nInformasi CPU\n"
    softw += "Physical cores   : " + str(psutil.cpu_count(logical=False)) + "\n"
    softw += "Total cores      : " + str(psutil.cpu_count(logical=True)) + "\n"
    cpufreq = psutil.cpu_freq()
    softw += f"Max Frequency    : {cpufreq.max:.2f}Mhz\n"
    softw += f"Min Frequency    : {cpufreq.min:.2f}Mhz\n"
    softw += f"Current Frequency: {cpufreq.current:.2f}Mhz\n\n"
    softw += "CPU Usage Per Core\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        softw += f"Core {i}  : {percentage}%\n"
    softw += "Total CPU Usage\n"
    softw += f"Semua Core: {psutil.cpu_percent()}%\n"

    softw += "\nBandwith Digunakan\n"
    softw += f"Unggah  : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    softw += f"Download: {get_size(psutil.net_io_counters().bytes_recv)}\n"

    svmem = psutil.virtual_memory()
    softw += "\nMemori Digunakan\n"
    softw += f"Total     : {get_size(svmem.total)}\n"
    softw += f"Available : {get_size(svmem.available)}\n"
    softw += f"Used      : {get_size(svmem.used)}\n"
    softw += f"Percentage: {svmem.percent}%\n"

    msg = await c.send_message(callback_query.from_user.id, f"<b>{softw}</b>")
    await asyncio.sleep(15)
    return await msg.delete()


async def cb_restart(client, callback_query):
    await callback_query.message.delete()
    await restart()


async def cb_gitpull(client, callback_query):
    await callback_query.message.delete()
    os.system(f"git pull")
    await restart()


async def cek_host(c, m):
    xx = await m.reply("Processing...")
    uname = platform.uname()
    softw = "Informasi Sistem\n"
    softw += f"Sistem   : {uname.system}\n"
    softw += f"Rilis    : {uname.release}\n"
    softw += f"Versi    : {uname.version}\n"
    softw += f"Mesin    : {uname.machine}\n"

    boot_time_timestamp = psutil.boot_time()

    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"Waktu Hidup: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}\n"

    softw += "\nInformasi CPU\n"
    softw += "Physical cores   : " + str(psutil.cpu_count(logical=False)) + "\n"
    softw += "Total cores      : " + str(psutil.cpu_count(logical=True)) + "\n"
    cpufreq = psutil.cpu_freq()
    softw += f"Max Frequency    : {cpufreq.max:.2f}Mhz\n"
    softw += f"Min Frequency    : {cpufreq.min:.2f}Mhz\n"
    softw += f"Current Frequency: {cpufreq.current:.2f}Mhz\n\n"
    softw += "CPU Usage Per Core\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        softw += f"Core {i}  : {percentage}%\n"
    softw += "Total CPU Usage\n"
    softw += f"Semua Core: {psutil.cpu_percent()}%\n"

    softw += "\nBandwith Digunakan\n"
    softw += f"Unggah  : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    softw += f"Download: {get_size(psutil.net_io_counters().bytes_recv)}\n"

    svmem = psutil.virtual_memory()
    softw += "\nMemori Digunakan\n"
    softw += f"Total     : {get_size(svmem.total)}\n"
    softw += f"Available : {get_size(svmem.available)}\n"
    softw += f"Used      : {get_size(svmem.used)}\n"
    softw += f"Percentage: {svmem.percent}%\n"

    await xx.edit(f"<b>{softw}</b>")
