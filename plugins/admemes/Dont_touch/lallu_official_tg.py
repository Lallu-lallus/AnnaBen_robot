
 
import re 
 
from pyromod import listen 
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters 
from pyrogram.errors import PeerIdInvalid, MessageIdInvalid

from bot.helpers import encode
 
@Client.on_message(filters.command("batch") & filters.private & ~filters.bot, group=3) 
async def batch(bot:Client, update:Message): 
 
    user_id = update.from_user.id 
 
    post1:Message = await bot.ask(chat_id=update.chat.id, text="Please Forward The First Post From The Channel (Where I Am an admin)", timeout=360) 
    if not post1: return 
 
    if not post1.forward_from_chat: 
 
        await update.reply_text("Please Forward The Message With Quotes (ie : Forwarded From ...)") 
        return 
 
    chat_id1 = post1.forward_from_chat.id 
    try : 
 
        msg_id1 = post1.forward_from_message_id 
        await bot.get_messages( 
            chat_id=chat_id1, 
            message_ids=msg_id1 
        ) 
    except PeerIdInvalid: 
        return await update.reply_text("Looks like Im Not A Member Of The Chat Where This Message Is Posted") 
    except MessageIdInvalid: 
        return await update.reply_text("Looks Like The Message You Forwarded No Longer Exists") 
    except Exception as e: 
        print(e) 
        return await update.reply_text("Something Went Wrong Please Try Again Later") 
 
    post2 = await bot.ask(chat_id=update.chat.id, text="Now Forward The Last Message From The Same Channel", timeout=360) 
    if not post2 : return 
 
    chat_id2 = post2.forward_from_chat.id 
    if not chat_id1==chat_id2 : 
        return await update.reply_text("These Two Messages Arent From The Same Chat") 
 
    try : 
 
        msg_id2 = post2.forward_from_message_id 
        await bot.get_messages( 
            chat_id=chat_id2, 
            message_ids=msg_id2 
        ) 
    except PeerIdInvalid: 
        return await update.reply_text("Looks like Im Not A Member Of The Chat Where This Message Is Posted") 
    except MessageIdInvalid: 
        return await update.reply_text("Looks Like The Message You Forwarded No Longer Exists") 
    except Exception as e: 
        print(e) 
        return await update.reply_text("Something Went Wrong Please Try Again Later") 
 
    if not msg_id1<=msg_id2: 
        return await update.reply_text("The First Message Has To Be Posted Above The Second In The Channel To Generate A Batch") 
 
    encoded = await encode(f"{str(chat_id1).replace('-100','')} {msg_id1} {msg_id2}") 
    url = f"https://t.me/DoraFilterBot?start={encoded}" 
 
    await update.reply_text(f"Woohoo... I've Successfully Generated A Link For Your Batch\n{url}\nPS:This Link Will Only Work As Long As I AM An Admin In The From Channel")
