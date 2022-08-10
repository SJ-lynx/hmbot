from hmtai import get
import random, os
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.environ['TOKEN']

bot = Bot(TOKEN)
dp = Dispatcher(bot)


forRandom = ["anal", "ass", "bdsm", "cum", "classic", "creampie", "manga", "femdom", "hentai", "incest", "masturbation", "public", "ero", "orgy", "elves", "yuri", "pantsu", "glasses",
             "cuckold", "blowjob", "boobjob", "footjob", "handjob", "boobs", "thighs", "pussy", "ahegao", "uniform", "gangbang", "tentacles", "nsfwNeko", "nsfwMobileWallpaper", "zettaiRyouiki"]

Random = KeyboardButton("Random")
Hentai = KeyboardButton("Hentai")
Neko = KeyboardButton("Neko")
Anal = KeyboardButton("Anal")
Ero = KeyboardButton("Ero")
Ass = KeyboardButton("Ass")
Gif = KeyboardButton("Gif")

Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    Random, Hentai, Neko, Anal, Ero, Ass, Gif)


@dp.message_handler(commands=['start'])
async def startcmd(message: Message):
    await bot.send_message(message.chat.id, "Hi {0.first_name}".format(message.chat), reply_markup=Menu)
    x = message.from_user.first_name
    await bot.send_message(-1001745065823, f"[{x}](tg://user?id={message.from_user.id})", parse_mode="markdown")


@dp.message_handler()
async def msgcmd(message: Message):
    if message.text == 'Random':
        await bot.send_photo(message.chat.id, get("hmtai", random.choice(forRandom)))
    elif message.text == 'Hentai':
        await bot.send_photo(message.chat.id, get("hmtai", "hentai"))
    elif message.text == 'Neko':
        await bot.send_photo(message.chat.id, get(random.choice(["hmtai", "nekos"]), "neko"))
    elif message.text == 'Anal':
        await bot.send_photo(message.chat.id, get("hmtai", "anal"))
    elif message.text == 'Ero':
        await bot.send_photo(message.chat.id, get("hmtai", "ero"))
    elif message.text == 'Ass':
        await bot.send_photo(message.chat.id, get("hmtai", "gangbang"))
    elif message.text == 'Gif':
        await bot.send_video(message.chat.id, get("hmtai", "gif"))

executor.start_polling(dp)
