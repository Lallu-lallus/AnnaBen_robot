#credits - @pro_editor_tg @Joel_TG
import os
import time
import random
import logging

from aiogram import Bot, Dispatcher, executor, types
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
from utils import Media, get_file_details, get_size
from pyrogram.errors import UserNotParticipant
logger = logging.getLogger(__name__)

#photo code kanged from @codes4ya Channel !
#Add atleast 10+ Telegraph Links below 👇


PHOTO = [
    "https://telegra.ph/file/56377c45b58f2d5121c28.jpg",
    "https://telegra.ph/file/96438c4d4c4b9a78505b9.jpg",
    "https://telegra.ph/file/e37fcf0c532b95a8dfb91.jpg",
    "https://telegra.ph/file/5fc1c6e2fdcd41db1772a.jpg",
    "https://telegra.ph/file/753fe4a57ed3934caa194.jpg",
    "https://telegra.ph/file/36b0d543462f2d5ffc6e9.jpg",
    "https://telegra.ph/file/6327ef11e0b1f70704364.jpg",
    "https://telegra.ph/file/18f12eeba6fcf227d32d6.jpg",
    "https://telegra.ph/file/d586cf7341cb3610da734.jpg",
    "https://telegra.ph/file/a9c8adab2dbe5f7bacd96.jpg",

]

bot = Bot(token=getenv("BOT_TOKEN"), parse_mode="HTML")

Client = Dispatcher(bot)
@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):

   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.command("start"))
async def start(bot, cmd):
    usr_cmdall1 = cmd.text
    if usr_cmdall1.startswith("/start subinps"):
        if AUTH_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
            try:
                user = await bot.get_chat_member(int(AUTH_CHANNEL), cmd.from_user.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="Sorry Sir, You are Banned to use me.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                ident, file_id = cmd.text.split("_-_-_-_")
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="**Please Join My Updates Channel to use this Bot!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url='https://t.me/tg_bots_updates')
                            ],
                            [
                                InlineKeyboardButton(" 🔄 Try Again", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="Something went Wrong.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        try:
            ident, file_id = cmd.text.split("_-_-_-_")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [
                    [
                        InlineKeyboardButton('🔍Search again🔎', switch_inline_query_current_chat=''),
                        InlineKeyboardButton('🤖More Bots🤖', url='https://t.me/tg_bots_updates')
                    ]
                    ]
                await bot.send_cached_media(
                    chat_id=cmd.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")
    elif len(cmd.command) > 1 and cmd.command[1] == 'subscribe':
        invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url='https://t.me/tg_bots_updates')
                    ]
                ]
            )
        )
    else:
        await cmd.reply_photo(
            photo=f"{random.choice(PHOTO)}",
            caption=START_MSG,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❔ How To Use Me ❔", url="https://t.me/tg_bots_updates")
                    ],
                    [
                        InlineKeyboardButton("©️CHANNEL", url="https://t.me/tg_bots_updates"),
                        InlineKeyboardButton("♻️GROUP", url="https://t.me/EDIT_REPO")
                    ],
                    [
                        InlineKeyboardButton("1 Dev", url="https://t.me/joinchat/Hn3YHLdbQf04MmM1"),
                        InlineKeyboardButton("2 Dev", url="https://t.me/darkz_angel")
                    ],
                    [
                        InlineKeyboardButton("➕ Add Me To Your Group ➕", url="https://t.me/Dqautofl_bot?startgroup=true")
                    ]
                ]
            )
        )


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')
@Client.on_message(filters.command('about'))
async def bot_info(bot, message):
    buttons = [
        [
            InlineKeyboardButton('Update Channel', url='https://t.me/tg_bots_updates'),
            InlineKeyboardButton('Source Code', url='https://github.com/Lallu-lallus/ALPHA-AUTO-FILTER-BOT')
        ]
        ]
    await message.reply(text="Language : <code>Python3</code>\nLibrary : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio</a>\nSource Code : <a href='https://github.com/Lallu-lallus/ALPHA-AUTO-FILTER-BOT'>Click here</a>\nUpdate Channel : <a href='https://t.me/tg_bots_updates'>ALPH_BOTZ</a> </b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
    await message.reply(text="Language : <code>Python3</code>\nLibrary : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio</a>\nSource Code : <a href='https://github.com/Lallu-lallus/ALPHA-AUTO-FILTER-BOT'>Click here</a>\nUpdate Channel : <a href='https://t.me/tg_bots_updates'>ALPH_BOTZ</a> </b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
@Client.message_handler(commands="id")

async def cmd_id(message: types.Message):

    """

    /id command handler for all chats

    :param message: Telegram message with "/id" command

    """

    if message.chat.id == message.from_user.id:

        await message.answer(f"Your Telegram ID is <code>{message.from_user.id}</code>")

    else:

        await message.answer(f"This {message.chat.type} chat ID is <code>{message.chat.id}</code>")

    logs.track("/id")
