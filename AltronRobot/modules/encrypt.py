import secureme
from AltronRobot.events import register


@register(pattern="^/encrypt ?(.*)")
async def encrypt(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        cmd = lel.text
    else:
        cmd = event.text.split(" ", 1)[1]
    k = secureme.encrypt(cmd)
    await event.reply(k)


@register(pattern="^/decrypt ?(.*)")
async def decrypt(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        ok = lel.text
    else:
        ok = event.text.split(" ", 1)[1]
    k = secureme.decrypt(ok)
    await event.reply(k)

__mod_name__ = "Tá´á´Ês"

__help__ = """
ðð¼ð»ðð²ð¿ðð:
  â² /encrypt: á´É´á´ÊÊá´á´ê± á´Êá´ É¢Éªá´ á´É´ á´á´xá´
  â² /decrypt: á´á´á´ÊÊá´á´ê± á´Êá´á´ Éªá´á´ê±ÊÊ á´á´ÊÊá´á´á´á´ á´á´xá´
"""
