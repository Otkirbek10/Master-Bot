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




@dp.message_handler(text = 'HA✅',state=Sherik.send)
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
    await bot.send_message(5012333108,f"Sherik kerak:\n\n🏅 Sherik: {fulln}\n📚 Texnologiya: {tecno}\n📥 Telegram: @{user}\n📞 Aloqa: {pone}\n🌐 Hudud: {manzil}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {ksb}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()
    
@dp.message_handler(text = 'YO\'Q❌',state='*')
async def yoq(message:types.Message):
    await message.answer("Qabul qilinmadi",reply_markup=menu)


@dp.callback_query_handler(text='send_ch')
async def ad_send(call:types.CallbackQuery):
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=CHANNELS[0])

@dp.message_handler(text = 'HA✅',state=Ish.send)
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
    await bot.send_message(5012333108,f"Ish joyi kerak:\n\n👨‍💻 Xodim: {name}\n🕑 Yosh: {age}\n📚 Texnologiya: {tex}\n📥 Telegram: @{user}\n📞 Aloqa: {phone}\n🌐 Hudud: {loc}\n💰 Narxi: {pric}\n👨🏻‍💻 Kasbi: {kasb}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()

@dp.message_handler(text = 'HA✅',state=Xodim.send)
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
    await bot.send_message(5012333108,f"Xodim kerak:\n\n🏢 Idora: {namei}\n📚 Texnologiya: {texi}\n📥 Telegram: @{user}\n📞 Aloqa: {phone}\n🌐 Hudud: {loc}\n✍️ Mas'ul: {mas_sh}\n🕰 Murojaat vaqti: {time}\n🕰 Ish vaqti: {timei}\n💰 Maosh: {maosh}\n➕ Qo'shimcha: {qosh}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()

@dp.message_handler(text = 'HA✅',state=Ustoz.send)
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
    await bot.send_message(5012333108,f"Ustoz kerak:\n\n👨‍💻 Shogird: {fname}\n🌐 Yosh: {age}\n📚 Texnologiya: {techno}\n📥 Telegram: @{user}\n📞 Aloqa: {phone}\n🌐 Hudud: {loc}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {prof}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()

@dp.message_handler(text = 'HA✅',state=Shogird.send)
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
    await bot.send_message(5012333108,f"Shogird kerak:\n\n🎓 Ustoz: {full}\n🌐 Yosh: {age}\n📚 Texnologiya: {texno}\n📥 Telegram: @{user}\n📞 Aloqa: {phne}\n🌐 Hudud: {mnl}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {ksb}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}",reply_markup=send_ad)
    await message.answer("Muvaffaqiyatli qabul qilindi",reply_markup=menu)
    await message.edit_reply_markup()
    await state.finish()
