from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from info import bot, call_py, COMMAND_HAND_LER, contact_filter
from plugins.Vc.handlers import skip_current_song, skip_item
from plugins.Vc.queues import QUEUE, clear_queue

@Client.on_message(contact_filter & filters.command(['skip'], prefixes=f"{COMMAND_HAND_LER}"))
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**🙄There's nothing in the queue to skip!**")
        elif op == 1:
            await m.reply("**😩Empty Queue, Leaving Voice Chat**")
        else:
            await m.reply(
                f"**⏭ Skipped** \n**🎧 Now playing** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ Removed the following songs from the Queue: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)        
      

@Client.on_message(contact_filter & filters.command(['end', 'stop'], prefixes=f"{COMMAND_HAND_LER}"))
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**😐End**")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**🤨Nothing is playing !**")

   
@Client.on_message(contact_filter & filters.command(['pause'], prefixes=f"{COMMAND_HAND_LER}"))
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ Paused.**\n\n• To resume playback, use the command » {HNDLR}resume"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**🤨Nothing is playing!**")
      

@Client.on_message(contact_filter & filters.command(['resume'], prefixes=f"{COMMAND_HAND_LER}"))
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ Resumed**\n\n• To pause playback, use the command » {COMMAND_HAND_LER}pause**"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**🙄 Nothing is currently paused!**")
