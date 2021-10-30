#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [Whois Telegram information bot by TeLe TiPs] (https://github.com/teletips/Whois-TeLeTiPs)

 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

whois=Client(
    "Whois",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@whois.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f'Heya {message.from_user.mention},\nMy name is <b>Whois</b>. I am here to provide Telegram information!\n\n<u><b>Commands</b></u>:\n/m - To get your information\n/u - To get user information (Reply to a forwarded message)\n/c - To get group/channel information (Reply to a forwarded message)'
    reply_markup = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('NEWS', url='https://t.me/teletipsofficialchannel')
        ]]
    )
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@whois.on_message(filters.command('m') & filters.private)
async def start(client, message):
    await message.reply(
        f"""        
<b>First name</b>: {message.from_user.first_name}
<b>Last name</b>: {message.from_user.last_name}
<b>Username</b>: {message.from_user.username}
<b>Telegram id</b>: <code>{message.from_user.id}</code>
<b>Phone number</b>: {message.from_user.phone_number}
<b>Language</b>: {message.from_user.language_code}
<b>Status</b>: {message.from_user.status}
<b>Data center id</b>: {message.from_user.dc_id}"""
)

@whois.on_message(filters.command('u') & filters.private)
async def start(client, message):
    await message.reply(
        f"""
<b>First name</b>: {message.reply_to_message.forward_from.first_name}
<b>Last name</b>: {message.reply_to_message.forward_from.last_name}
<b>Username</b>: {message.reply_to_message.forward_from.username}
<b>Telegram id</b>: <code>{message.reply_to_message.forward_from.id}</code>
<b>Phone number</b>: {message.reply_to_message.forward_from.phone_number}
<b>Language</b>: {message.reply_to_message.forward_from.language_code}
<b>Status</b>: {message.reply_to_message.forward_from.status}
<b>Data center id</b>: {message.reply_to_message.forward_from.dc_id}"""
)

@whois.on_message(filters.command('c'))
async def start(client, message):
    await message.reply(
        f"""
<b>Name</b>: {message.reply_to_message.forward_from_chat.title}
<b>Username</b>: {message.reply_to_message.forward_from_chat.username}
<b>Telegram id</b>: {message.reply_to_message.forward_from_chat.id}
<b>Type</b>: {message.reply_to_message.forward_from_chat.type}
<b>Data center id</b>: {message.reply_to_message.forward_from_chat.dc_id}
"""
)
 
print("Whois is alive!")
whois.run()

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
