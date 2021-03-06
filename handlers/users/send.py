from email import message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboards.inline.add import send_ad
from states.state import Sherik,Ish,Xodim,Ustoz,Shogird
from keyboards.default.buttons import menu
from data.config import CHANNELS
from data.config import BOT_TOKEN
bot = Bot(token=BOT_TOKEN)
from loader import dp
import re




@dp.message_handler(text = 'HAâ',state=Sherik.send)
async def ha(message:types.Message,state:FSMContext):
    data = await state.get_data()
    fulln = data.get('ism_familiya')
    tecno = data.get('texno')
    pone = data.get('phone')
    manzil = data.get('hudud')
    price = data.get('narx')
    ksb = data.get('kasb')
    time = data.get('vaqt')
    goal = data.get('maqsad')
    user = message.from_user.username
    await bot.send_message(5012333108,f"Sherik kerak:\n\nð Sherik: {fulln}\nð Texnologiya: {tecno}\nð¥ Telegram: @{user}\nð Aloqa: {pone}\nð Hudud: {manzil}\nð° Narxi: {price}\nð¨ð»âð» Kasbi: {ksb}\nð° Murojaat qilish vaqti: {time}\nð Maqsad: {goal}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()
    
@dp.message_handler(text = 'YO\'Qâ',state='*')
async def yoq(message:types.Message):
    await message.answer("Qabul qilinmadi",reply_markup=menu)


@dp.callback_query_handler(text='send_ch')
async def ad_send(call:types.CallbackQuery):
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=CHANNELS[0])

@dp.message_handler(text = 'HAâ',state=Ish.send)
async def ha(message:types.Message,state:FSMContext):
    data = await state.get_data()
    name = data.get('xodim')
    age = data.get('yosh')
    tex = data.get('texno')
    phone = data.get('phone')
    loc = data.get('hudud')
    pric = data.get('narx')
    kasb = data.get('kasb')
    time = data.get('vaqt')
    goal = data.get('maqsad')
    user = message.from_user.username
    await bot.send_message(5012333108,f"Ish joyi kerak:\n\nð¨âð» Xodim: {name}\nð Yosh: {age}\nð Texnologiya: {tex}\nð¥ Telegram: @{user}\nð Aloqa: {phone}\nð Hudud: {loc}\nð° Narxi: {pric}\nð¨ð»âð» Kasbi: {kasb}\nð° Murojaat qilish vaqti: {time}\nð Maqsad: {goal}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()

@dp.message_handler(text = 'HAâ',state=Xodim.send)
async def ha(message:types.Message,state:FSMContext):
    data = await state.get_data()
    namei = data.get('idora')
    texi = data.get('texno')
    phone = data.get('phone')
    loc = data.get('hudud')
    mas_sh = data.get('masul')
    time = data.get('vaqt')
    timei = data.get('ivaqt')
    maosh = data.get('maosh')
    qosh = data.get("qosh")
    user = message.from_user.username
    await bot.send_message(5012333108,f"Xodim kerak:\n\nð¢ Idora: {namei}\nð Texnologiya: {texi}\nð¥ Telegram: @{user}\nð Aloqa: {phone}\nð Hudud: {loc}\nâï¸ Mas'ul: {mas_sh}\nð° Murojaat vaqti: {time}\nð° Ish vaqti: {timei}\nð° Maosh: {maosh}\nâ Qo'shimcha: {qosh}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()

@dp.message_handler(text = 'HAâ',state=Ustoz.send)
async def ha(message:types.Message,state:FSMContext):
    data = await state.get_data()
    fname = data.get('ism_familiya')
    age = data.get('yosh')
    techno = data.get('texno')
    phone = data.get('phone')
    loc = data.get('hudud')
    price = data.get('narx')
    prof = data.get('kasb')
    time = data.get('vaqt')
    goal = data.get('maqsad')
    user = message.from_user.username
    await bot.send_message(5012333108,f"Ustoz kerak:\n\nð¨âð» Shogird: {fname}\nð Yosh: {age}\nð Texnologiya: {techno}\nð¥ Telegram: @{user}\nð Aloqa: {phone}\nð Hudud: {loc}\nð° Narxi: {price}\nð¨ð»âð» Kasbi: {prof}\nð° Murojaat qilish vaqti: {time}\nð Maqsad: {goal}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()

@dp.message_handler(text = 'HAâ',state=Shogird.send)
async def ha(message:types.Message,state:FSMContext):
    data = await state.get_data()
    data = await state.get_data()
    full = data.get('ism')
    age = data.get('yosh')
    texno = data.get('texno')
    phne = data.get('phone')
    mnl = data.get('hudud')
    price = data.get('narx')
    ksb = data.get('kasb')
    time = data.get('vaqt')
    goal = data.get('maqsad')
    user = message.from_user.username
    await bot.send_message(5012333108,f"Shogird kerak:\n\nð Ustoz: {full}\nð Yosh: {age}\nð Texnologiya: {texno}\nð¥ Telegram: @{user}\nð Aloqa: {phne}\nð Hudud: {mnl}\nð° Narxi: {price}\nð¨ð»âð» Kasbi: {ksb}\nð° Murojaat qilish vaqti: {time}\nð Maqsad: {goal}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()
