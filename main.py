from hmtai import get
import random, os
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

TOKEN = os.environ['TOKEN']
CHANNEL_ID = int(os.environ['CHANNEL_ID'])
CHANNEL_LINK = os.environ['CHANNEL_LINK']

bot = Bot(TOKEN)
dp = Dispatcher(bot)

sub = InlineKeyboardButton('➕Subscribe', url=CHANNEL_LINK)
con = InlineKeyboardButton('✅Confirm', callback_data='confirm')

checksub = InlineKeyboardMarkup(row_width=1)
checksub.insert(sub)
checksub.insert(con)

forRandom = ["anal", "ass", "bdsm", "cum", "classic", "creampie", "manga", "femdom", "hentai", "incest", "masturbation", "public", "ero", "orgy", "elves", "yuri", "pantsu", "glasses", "cuckold", "blowjob", "boobjob", "footjob", "handjob", "boobs", "thighs", "pussy", "ahegao", "uniform", "gangbang", "tentacles", "nsfwNeko", "nsfwMobileWallpaper", "zettaiRyouiki"]

Random = KeyboardButton("Random")
Hentai = KeyboardButton("Hentai")
Neko = KeyboardButton("Neko")
Anal = KeyboardButton("Anal")
Ero = KeyboardButton("Ero")
Ass = KeyboardButton("Ass")
Gif = KeyboardButton("Gif")

Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(Random, Hentai, Neko, Anal, Ero, Ass, Gif)


def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(commands=['start'])
async def startcmd(message: Message):
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Hi {0.first_name}".format(message.from_user), reply_markup=Menu)
    else:
        await bot.send_message(message.from_user.id, "Hi {0.first_name}\nTo use the bot, subscribe to the channel".format(message.from_user), reply_markup=checksub)


@dp.callback_query_handler(text="confirm")
async def confirm(callback_query: CallbackQuery):
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=callback_query.from_user.id)):
        await bot.send_message(callback_query.from_user.id, "Thank you for subscribing to the channel!", reply_markup=Menu)
    await bot.answer_callback_query(callback_query.id)


# gangbang
@dp.message_handler()
async def msgcmd(message: Message):
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        if message.text == 'Random':
            await bot.send_photo(message.from_user.id, get("hmtai", random.choice(forRandom)))
        elif message.text == 'Hentai':
            await bot.send_photo(message.from_user.id, get("hmtai", "hentai"))
        elif message.text == 'Neko':
            await bot.send_photo(message.from_user.id, get(random.choice(["hmtai","nekos"]), "neko"))
        elif message.text == 'Anal':
            await bot.send_photo(message.from_user.id, get("hmtai", "anal"))
        elif message.text == 'Ero':
            await bot.send_photo(message.from_user.id, get("hmtai", "ero"))
        elif message.text == 'Ass':
            await bot.send_photo(message.from_user.id, get("hmtai", "gangbang"))
        elif message.text == 'Gif':
            await bot.send_video(message.from_user.id, get("hmtai", "gif"))
    else:
        await bot.send_message(message.from_user.id, "To use the bot, subscribe to the channel", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Subscribe✅', url=CHANNEL_LINK)))


if __name__ == '__main__':
    executor.start_polling(dp)
