from ubot import *


@PY.BOT("prem")
@PY.SELLER
async def _(client, message):
    await prem_user(client, message)
@PY.UBOT("prem")
@PY.SELLER
async def _(client, message):
    await prem_user(client, message)


@PY.BOT("delprem")
@PY.SELLER
async def _(client, message):
    await unprem_user(client, message)
@PY.UBOT("delprem")
@PY.SELLER
async def _(client, message):
    await unprem_user(client, message)


@PY.BOT("getprem")
@PY.OWNER
async def _(client, message):
    await get_prem_user(client, message)
@PY.UBOT("getprem")
@PY.OWNER
async def _(client, message):
    await get_prem_user(client, message)


@PY.BOT("seles")
@PY.OWNER
async def _(client, message):
    await seles_user(client, message)
@PY.UBOT("seles")
@PY.OWNER
async def _(client, message):
    await seles_user(client, message)


@PY.BOT("delseles")
@PY.OWNER
async def _(client, message):
    await unseles_user(client, message)
@PY.UBOT("delseles")
@PY.OWNER
async def _(client, message):
    await unseles_user(client, message)


@PY.BOT("getseles")
@PY.OWNER
async def _(client, message):
    await get_seles_user(client, message)
@PY.UBOT("getseles")
@PY.OWNER
async def _(client, message):
    await get_seles_user(client, message)


@PY.BOT("setexp")
@PY.SELLER
async def _(client, message):
    await expired_add(client, message)
@PY.UBOT("setexp")
@PY.SELLER
async def _(client, message):
    await expired_add(client, message)


@PY.BOT("cek")
@PY.SELLER
async def _(client, message):
    await expired_cek(client, message)
@PY.UBOT("cek")
@PY.SELLER
async def _(client, message):
    await expired_cek(client, message)


@PY.BOT("delexp")
@PY.SELLER
async def _(client, message):
    await un_expired(client, message)
@PY.UBOT("delexp")
@PY.SELLER
async def _(client, message):
    await un_expired(client, message)


@PY.CALLBACK("restart")
async def _(client, callback_query):
    await cb_restart(client, callback_query)


@PY.CALLBACK("gitpull")
async def _(client, callback_query):
    await cb_gitpull(client, callback_query)


@PY.BOT("bcast")
@PY.OWNER
async def _(client, message):
    await bacotan(client, message)
