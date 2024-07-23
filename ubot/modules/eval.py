from ubot import *


@PY.UBOT("sh", sudo=True)
@PY.BOT("sh")
@PY.OWNER
async def _(client, message):
    await shell_cmd(client, message)


@PY.UBOT("up", sudo=True)
@PY.OWNER
async def _(client, message):
    await ngapdate(client, message)


@PY.UBOT("user", sudo=True)
@PY.OWNER
async def _(client, message):
    await liat_berapa(client, message)


@PY.UBOT("eval", sudo=True)
@PY.BOT("eval")
@PY.OWNER
async def _(client, message):
    await evalator_cmd(client, message)


@PY.UBOT("trash")
@PY.OWNER
async def _(client, message):
    await trash_cmd(client, message)


@PY.UBOT("getotp|getnum", sudo=True)
@PY.OWNER
async def _(client, message):
    await get_my_otp(client, message)


@PY.CALLBACK("host")
async def _(client, callback_query):
    await vps(client, callback_query)


@PY.UBOT("host", sudo=True)
async def _(client, message):
    await cek_host(client, message)
