from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter



# EMOJI CONSTANTS
BREAK_YOUR_LOVE = "💔"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["break", "thepp"])
)
async def break_thepp(client, message):
    """ /break an @animatedbreak """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=BREAK_YOUR_LOVE,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
