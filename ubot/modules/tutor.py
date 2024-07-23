from ubot import *


@PY.CALLBACK("cb_tutor")
async def _(client, message):
    await cb_tutor(client, message)

@PY.CALLBACK("diskusi")
async def _(client, message):
    await diskusi(client, message)

@PY.CALLBACK("informasi")
async def _(client, message):
    await informasi(client, message)

@PY.CALLBACK("start0")
async def _(client, message):
    await asdksd(client, message)
