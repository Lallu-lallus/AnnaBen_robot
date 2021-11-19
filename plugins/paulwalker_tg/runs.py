import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "A bear walks into a bar and says, Give me a whiskey and … cola.",
    "A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”..",
    "Hear about the new restaurant called Karma?",
    "Did you hear about the actor who fell through the floorboards?",
    "Why don’t scientists trust atoms?",
    "Why did the chicken go to the séance?",
    "Where are average things manufactured?",
    "How do you drown a hipster?",
    "What sits at the bottom of the sea and twitches?",
    "What does a nosy pepper do?ക് ",
    "How does Moses make tea?.",
    "What kind of exercise do lazy people do?",
    "Why don’t Calculus majors throw house parties?",
    "What do you call a parade of rabbits hopping backwards?.",
    "What does Charles Dickens keep in his spice rack?",
    "What’s the different between a cat and a comma?",
    "Why should the number 288 never be mentioned?.",
    "What did the Tin Man say when he got run over by a steamroller?...!",
    "What did the Buddhist say to the hot dog vendor?..!",
    "What did the left eye say to the right eye?",
    "What do you call a magic dog?",
    "What did the shark say when he ate the clownfish?",
    "What do you call a fake noodle?..",
    "What do you call a pony with a cough?.",
    "What did one hat say to the other?....",
    "How do poets say hello?.",
    "Why do bees have sticky hair?.\
    Because they use honeycombs.",
    "How does a rabbi make his coffee?.\
    Hebrews it.",
    "I got my daughter a fridge for her birthday.", 
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
