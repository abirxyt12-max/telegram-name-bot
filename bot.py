import os
import telebot
from telebot import types

BOT_TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

names = [
    "Emily Carter",
    "Olivia Bennett",
    "Ava Mitchell",
    "Sophia Anderson",
    "Isabella Parker",
    "Mia Thompson",
    "Charlotte Wilson",
    "Amelia Davis",
    "Harper Morgan",
    "Evelyn Brooks",
    "Abigail Foster",
    "Ella Richardson",
    "Scarlett Hayes",
    "Grace Cooper",
    "Chloe Peterson",
    "Lily Collins",
    "Madison Reed",
    "Aria Bailey",
    "Nora Jenkins",
    "Zoey Phillips",
    "Hannah Murphy",
    "Layla Stewart",
    "Ellie Morris",
    "Riley Turner",
    "Victoria Ward",
    "Lillian Scott",
    "Addison Kelly",
    "Aubrey Sanders",
    "Stella Price",
    "Natalie Bennett",
    "Leah Coleman",
    "Audrey Parker",
    "Claire Evans",
    "Lucy Harrison",
    "Brooklyn Simmons",
    "Samantha Russell",
    "Caroline Griffin",
    "Kennedy Hayes",
    "Maya Patterson",
    "Sarah Hamilton",
    "Allison Graham",
    "Anna Wallace",
    "Gabriella Woods",
    "Hailey Bryant",
    "Elizabeth Harper",
    "Savannah Fisher",
    "Skylar Mason",
    "Julia Reynolds",
    "Ariana Chapman",
    "Kaylee Robertson",
    "Serenity Webb",
    "Cora Washington",
    "Piper Lawson",
    "Madeline Franklin",
    "Jade Henderson",
    "Vivian Crawford",
    "Sophie Crawford",
    "Delilah Armstrong",
    "Ruby Warren",
    "Alice Porter",
    "Autumn Carpenter",
    "Nevaeh West",
    "Natalia Johnston",
    "Everly Douglas",
    "Ivy Williamson",
    "Bella Montgomery",
    "Clara Stephens",
    "Caroline Chandler",
    "Genesis Lambert",
    "Naomi Wheeler",
    "Eliana Fuller",
    "Quinn Sullivan",
    "Lydia Morrison",
    "Eliza Burke",
    "Sadie Fisher",
    "Josephine McCarthy",
    "Piper Davidson",
    "Rose Franklin",
    "Reagan Morrison",
    "Emery Nichols",
    "Isabelle Ferguson",
    "Maria Lawrence",
    "Julia Garrett",
    "Katherine Dawson",
    "Brianna Elliott",
    "Melanie Rhodes",
    "Jasmine Spencer",
    "Paige Thornton",
    "Valeria Douglas",
    "Rachel Pearson",
    "Nicole Bennett",
    "Lauren Maxwell",
    "Megan Sullivan",
    "Rebecca Hamilton",
    "Ashley Donovan",
    "Jessica Palmer",
    "Amanda Russell",
    "Taylor Griffin",
    "Kimberly Lawson",
    "Stephanie Warren",
    # Add 1000 more US-style female names

first_names = [
    "Madison", "Brianna", "Camila", "Kennedy", "Peyton",
    "Skylar", "Savannah", "Aaliyah", "Allison", "Kayla",
    "Mackenzie", "Kylie", "Peyton", "Aubree", "Sienna",
    "Luna", "Violet", "Hazel", "Aurora", "Paisley",
    "Willow", "Everleigh", "Athena", "Arianna", "Peyton",
    "Ruby", "Alice", "Naomi", "Elena", "Mackenzie",
    "Faith", "Jasmine", "Adeline", "Alyssa", "Molly",
    "Clara", "Brielle", "Melody", "Natalie", "Kendall",
    "Morgan", "Kelsey", "Jocelyn", "Lillian", "Valerie",
    "Isla", "Rose", "Julia", "Samantha", "Delaney"
]

last_names = [
    "Adams", "Allen", "Baker", "Barnes", "Bell",
    "Bishop", "Black", "Bowman", "Bradley", "Brooks",
    "Brown", "Burton", "Butler", "Campbell", "Carson",
    "Carter", "Clark", "Clayton", "Collins", "Cook"
]

for first in first_names:
    for last in last_names:
        full_name = f"{first} {last}"
        if full_name not in names:
            names.append(full_name)
]

user_index = {}

def main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            "🎲 Get Name",
            callback_data="get_name"
        )
    )
    return keyboard

@bot.message_handler(commands=["start"])
def start(message):
    user_index[message.from_user.id] = 0
    bot.send_message(
        message.chat.id,
        "🇺🇸 US Girl Name Generator\n\nClick the button below to get a name.",
        reply_markup=main_keyboard()
    )

@bot.callback_query_handler(func=lambda call: call.data == "get_name")
def get_name(call):
    user_id = call.from_user.id

    if user_id not in user_index:
        user_index[user_id] = 0

    index = user_index[user_id]

    if index >= len(names):
        bot.answer_callback_query(
            call.id,
            "All 100 names have been used."
        )
        return

    number = index + 1
    name = names[index]

    text = f"🇺🇸 Name #{number}\n\n👤 {name}"

    keyboard = types.InlineKeyboardMarkup()

    copy_button = types.InlineKeyboardButton(
        "📋 Copy Name",
        copy_text=types.CopyTextButton(text=name)
    )

    next_button = types.InlineKeyboardButton(
        "🎲 Get Next Name",
        callback_data="get_name"
    )

    keyboard.row(copy_button)
    keyboard.row(next_button)

    bot.edit_message_text(
        text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=keyboard
    )

    user_index[user_id] += 1
    bot.answer_callback_query(call.id)

@bot.message_handler(commands=["reset"])
def reset(message):
    user_index[message.from_user.id] = 0

    bot.send_message(
        message.chat.id,
        "🔄 Reset complete!\n\nYou can start again from Name #1.",
        reply_markup=main_keyboard()
    )

print("🤖 Bot is running...")
bot.infinity_polling()
