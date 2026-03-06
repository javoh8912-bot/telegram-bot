import asyncio
import logging
import sys
import btns
from os import getenv
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = getenv["BOT_TOKEN"]

dp = Dispatcher()






















@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Congratulations! You subscribed to Jahon seriallari. \n\nUse /off to pause your subscription.", reply_markup=btns.start_Btns)
    await message.answer_sticker(sticker="AAMCAgADGQEAASAjCGktGBlFYIanse1J1UuBVzkeomXPAAJmXQAC_N5hSZF2gZmqUIo0AQAHbQADNgQ", caption="Want to create your own bot?\nGo to @Manybot")
    
@dp.message(F.text == "💻Menu💻")
async def start_handler(message: Message):
    await message.answer("💻", reply_markup=btns.menu_btns)







@dp.message(F.text == "💫 Yulduzlar jangi ⚔️")
async def yulduz_handler(message: Message):
    if message.text == "💫 Yulduzlar jangi ⚔️":
        await message.answer_photo(photo="https://i.pinimg.com/736x/5b/29/10/5b291061fe73d4f1533862d4318fdf43.jpg", reply_markup=btns.yulduz_btns)





@dp.message(F.text == "🦍 Monterverse 🦖")
async def monster_handler(message: Message):
    if message.text == "🦍 Monterverse 🦖":
        await message.answer_photo(photo="https://static0.cbrimages.com/wordpress/wp-content/uploads/2024/02/godzilla-and-kong-running-together-in-godzilla-x-kong-new-empire.jpg?&fit=crop&w=1200&h=675", reply_markup=btns.monster_keyboard)





@dp.message(F.text == "🔴 Marvel Studios 🔴")
async def marvel_handler(message: Message):
    if message.text == "🔴 Marvel Studios 🔴":
        await message.answer_photo(photo="https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1E54gd.img?w=2000&h=1000&m=4&q=79", reply_markup=btns.marvel_keyboard)






@dp.message(F.text == "🔵 DC Comics 🔵")
async def dc_handler(message: Message):
    if message.text == "🔵 DC Comics 🔵":
        await message.answer_photo(photo="https://i.ytimg.com/vi/I40jL1n_bR0/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGDMgTShyMA8=&amp;rs=AOn4CLDRJq5P4M8nvT6aDR4k76TJk5iFQw", reply_markup=btns.dc_keyboard)



@dp.message(F.text == "⚫️ Boshqa Filmlar ⚫️")
async def boshqa_handler(message: Message):
    if message.text == "⚫️ Boshqa Filmlar ⚫️":
        await message.answer_photo(photo="https://i.ytimg.com/vi/LgYOmoQh3rE/maxresdefault.jpg", reply_markup=btns.boshqa_keyboard)



@dp.message(F.text == "🎞Seriallar🎞")
async def serial_handler(message: Message):
    if message.text == "🎞Seriallar🎞":
        await message.answer(text="🎞", reply_markup=btns.seriallar_key)







@dp.message(F.text == "🎬Filmlar🎬")
async def film_handler(message: Message):
    if message.text == "🎬Filmlar🎬":
        await message.answer_photo(photo="https://i.ytimg.com/vi/rvH4f1xT_gY/maxresdefault.jpg", reply_markup=btns.filmlar_key)


@dp.message(F.text == "➕Qo'shimcha➕")
async def qoshimcha_handler(message: Message):
    if message.text == "➕Qo'shimcha➕":
        await message.answer_photo(photo="https://play-lh.googleusercontent.com/CCTJoRwjbQbAE8S4Gbv0NMU857WbQl6d5IFrAPuxy4s6G6jNdvob5jGpuL_oJRxfng=w7680-h4320", reply_markup=btns.qoshimcha_key)




@dp.message(F.text == "💻ADMIN💻")
async def admin_handler(message: Message):
    await message.answer(f"{"💻ADMIN💻"}\n{"@theDilmuorodov"}")





@dp.message(F.text == "Go Back")
async def back_handeler(message: Message):
    await message.answer(text="💻", reply_markup=btns.menu_btns)






async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())