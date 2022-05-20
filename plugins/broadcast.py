

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from helper.manjeet import client as manjeet
from config import OWNER_IDS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in OWNER_IDS:
        return
    else:
        wtf = await message.reply("`Stɑɤtɩŋʛ Ɓɤøɑɗƈɑst ...`")
        if not message.reply_to_message:
            await wtf.edit("**__YOU ARE NOT MY OWNER...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in manjeet.iter_dialogs():
            try:
                await manjeet.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"♥️ `Broadcasted Successfully` \n\n**🚩 Sent:** `{sent}` Ƈɦɑts \n**🚩 Failed:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`gcast succesfully` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")
