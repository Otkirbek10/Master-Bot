
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from keyboards.default.buttons import menu,javob
from states.state import Sherik,Ish,Xodim,Ustoz,Shogird
import re

from loader import dp 

@dp.message_handler(text = 'Sherik kerak',state='*')
async def do_sherik(message:types.Message):
    await message.answer('Sherik topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi.\nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va\narizangiz Adminga yuboriladi.')
    await message.answer("Ism familiyangizni kiriting")
    await Sherik.ism_familiya.set()

@dp.message_handler(state= Sherik.ism_familiya)
async def ismf(message:types.Message,state:FSMContext):
    ism_familiya = message.text
    await state.update_data(
        {'ism_familiya': ism_familiya}
    )
    await message.answer(f"📚 Texnologiya:\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating.\nMasalan: Java, C++, C#")
    await Sherik.next()

@dp.message_handler(state = Sherik.texno)
async def texnolog(message:types.Message,state:FSMContext):
    texno = message.text
    await state.update_data(
        {'texno': texno}
    )
    await message.answer(f"📞 Aloqa:\nTelefon raqamingizni qoldiring\nMasalan, +998941997111")
    await Sherik.next()

@dp.message_handler(state=Sherik.phone)
async def get_phone(message:types.Message,state:FSMContext):
    phone = message.text
    num =  "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"
    if re.match(num,phone):
        await state.update_data(
            {'phone': phone}
        )
        await message.answer(f"🌐 Hudud:\nQaysi hududdansiz?\nViloyat nomini,Toshkent shahar yoki Respublikani kiriting.")
        await Sherik.next()
    else:
        await message.answer("Siz mavjud bo'lmagan raqam kiritdingiz!")
        await Sherik.phone
    

@dp.message_handler(state=Sherik.hudud)
async def get_loc(message:types.Message,state:FSMContext):
    hudud = message.text
    await state.update_data(
        {'hudud': hudud}
    )
    await message.answer(f"💰 Narxi:\nTo'lov qilasizmi yoki tekinmi?\nSummani kiriting.")
    await Sherik.next()
@dp.message_handler(state=Sherik.narx)
async def get_p(message:types.Message,state:FSMContext):
    narx = message.text
    await state.update_data(
        {'narx': narx}
    )
    await message.answer(f"👨🏻‍💻 Kasbi:\nO'qiysizmi yoki ishlaysizmi?\nMasalan:Talaba")
    await Sherik.next()
@dp.message_handler(state=Sherik.kasb)
async def ask_kasb(message:types.Message,state:FSMContext):
    kasb = message.text
    await state.update_data(
        {'kasb': kasb}
    )
    await message.answer(f"🕰 Murojaat qilish vaqti:\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 00:00 - 02:00")
    await Sherik.next()
@dp.message_handler(state=Sherik.vaqt)
async def ask_vaqt(message:types.Message,state:FSMContext):
    vaqt = message.text
    await state.update_data(
        {'vaqt': vaqt}
    )
    await message.answer(f"🔎 Maqsad:\nMaqsadingizni qisqacha yozing")
    await Sherik.next()

@dp.message_handler(state=Sherik.maqsad)
async def ask_m(message:types.Message,state:FSMContext):
    maqsad = message.text
    await state.update_data(
        {'maqsad':maqsad}
    )
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
    await message.answer(f"Sherik kerak:\n\n🏅 Sherik: {fulln}\n📚 Texnologiya: {tecno}\n📥 Telegram: @{user}\n📞 Aloqa: {pone}\n🌐 Hudud: {manzil}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {ksb}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}")
    await message.answer("Barcha ma'lumotlar to'grimi?",reply_markup=javob)
    await Sherik.next()

#Ish joyi kerak
@dp.message_handler(text = 'Ish joyi kerak',state='*')
async def ish(message:types.Message):
    await message.answer("Ish joyi topish uchun ariza berish\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ism,familiyangizni kiriting")
    await Ish.xodim.set()

@dp.message_handler(state=Ish.xodim)
async def xp(message:types.Message,state:FSMContext):
    xodim = message.text
    await state.update_data(
        {'xodim':xodim}
    )
    await message.answer("🕑 Yosh\nYoshingizni kiriting\nMasalan 16")
    await Ish.next()

@dp.message_handler(state=Ish.yosh)
async def xp(message:types.Message,state:FSMContext):
    yosh = message.text
    await state.update_data(
        {'yosh':yosh}
    )
    await message.answer(f"📚 Texnologiya:\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating.\nMasalan: Java, C++, C#")
    await Ish.next()

@dp.message_handler(state=Ish.texno)
async def tech(message:types.Message,state:FSMContext):
    texno =  message.text
    await state.update_data(
        {'texno':texno}
    )
    await message.answer(f"📞 Aloqa:\nTelefon raqamingizni qoldiring\nMasalan, +998941997111")
    await Ish.next()

@dp.message_handler(state = Ish.phone)
async def ph(message:types.Message,state:FSMContext):
    phone = message.text
    num = "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"
    if re.match(num,phone):
        await state.update_data(
            {'phone':phone}
        )
        await message.answer(f"🌐 Hudud:\nQaysi hududdansiz?\nViloyat nomini,Toshkent shahar yoki Respublikani kiriting.")
        await Ish.next()
    else:
        await message.answer("Siz mavjud bo'lmagan raqam kiritdingiz")
        await Ish.phone
   

@dp.message_handler(state=Ish.hudud)
async def hu(message:types.Message,state:FSMContext):
    hudud = message.text
    await state.update_data(
        {'hudud':hudud}
    )
    await message.answer(f"💰 Narxi:\nTo'lov qilasizmi yoki tekinmi?\nSummani kiriting.")
    await Ish.next()

@dp.message_handler(state=Ish.narx)
async def na(message:types.Message,state:FSMContext):
    narx = message.text
    await state.update_data(
        {'narx':narx}
    )
    await message.answer(f"👨🏻‍💻 Kasbi:\nO'qiysizmi yoki ishlaysizmi?\nMasalan:Talaba")
    await Ish.next()

@dp.message_handler(state=Ish.kasb)
async def ka(message:types.Message,state:FSMContext):
    kasb = message.text
    await state.update_data(
        {'kasb':kasb}
    )
    await message.answer(f"🕰 Murojaat qilish vaqti:\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 00:00 - 02:00")
    await Ish.next()

@dp.message_handler(state=Ish.vaqt)
async def fv(message:types.Message,state:FSMContext):
    vaqt = message.text
    await state.update_data(
        {'vaqt':vaqt}
    )
    await message.answer(f"🔎 Maqsad:\nMaqsadingizni qisqacha yozing")
    await Ish.next()

@dp.message_handler(state=Ish.maqsad)
async def maq(message:types.Message,state:FSMContext):
    maqsad = message.text
    await state.update_data(
        {'maqsad':maqsad}
    )
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
    await message.answer(f"Ish joyi kerak:\n\n👨‍💻 Xodim: {name}\n🕑 Yosh: {age}\n📚 Texnologiya: {tex}\n📥 Telegram: @{user}\n📞 Aloqa: {phone}\n🌐 Hudud: {loc}\n💰 Narxi: {pric}\n👨🏻‍💻 Kasbi: {kasb}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}")
    await message.answer("Barcha ma'lumotlar to'grimi?",reply_markup=javob)
    await Ish.next()

#Xodim kerak
@dp.message_handler(text = 'Xodim kerak',state='*')
async def xodim(message:types.Message):
    await message.answer("Xodim topish uchun ariza berish\nHozir sizga birnecha savollar beriladi. Har biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("🏢 Idora nomini yozing")
    await Xodim.idora.set()

@dp.message_handler(state=Xodim.idora)
async def idora(message:types.Message,state:FSMContext):
    idora = message.text
    await state.update_data(
        {'idora':idora}
    )
    await message.answer("📚  Texnologiya:\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating.\nMasalan Java, C++, C#")
    await Xodim.next()
@dp.message_handler(state=Xodim.texno)
async def tec(message:types.Message,state:FSMContext):
    texno = message.text
    await state.update_data(
        {'texno':texno}
    )
    await message.answer(f"📞 Aloqa:\nTelefon raqamingizni qoldiring\nMasalan, +998941997111")
    await Xodim.next()

@dp.message_handler(state=Xodim.phone)
async def tec(message:types.Message,state:FSMContext):
    phone = message.text
    num = "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"
    if re.match(num,phone):
        await state.update_data(
            {'phone':phone}
        )
        await message.answer(f"🌐 Hudud:\nQaysi hududdansiz?\nViloyat nomini,Toshkent shahar yoki Respublikani kiriting.")
        await Xodim.next()
    else:
        await message.answer("Siz mavjud bo'lmagan raqam kiritdingiz")
        await Xodim.phone
    

@dp.message_handler(state=Xodim.hudud)
async def tec(message:types.Message,state:FSMContext):
    hudud = message.text
    await state.update_data(
        {'hudud':hudud}
    )
    await message.answer("✍️Mas'ul ism-sharifi ?")
    await Xodim.next()

@dp.message_handler(state=Xodim.masul)
async def mas(message:types.Message,state:FSMContext):
    masul = message.text
    await state.update_data(
        {'masul':masul}
    )
    await message.answer(f"🕰 Murojaat qilish vaqti:\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 00:00 - 02:00")
    await Xodim.next()

@dp.message_handler(state=Xodim.vaqt)
async def mas(message:types.Message,state:FSMContext):
    vaqt = message.text
    await state.update_data(
        {'vaqt':vaqt}
    )
    await message.answer("🕰 Ish vaqtini kiriting?")
    await Xodim.next()

@dp.message_handler(state=Xodim.ivaqt)
async def i(message:types.Message,state:FSMContext):
    ivaqt = message.text
    await state.update_data(
        {'ivaqt':ivaqt}
    )
    await message.answer("💰 Maoshni kiriting")
    await Xodim.next()

@dp.message_handler(state=Xodim.maosh)
async def pul(message:types.Message,state:FSMContext):
    maosh = message.text
    await state.update_data(
        {'maosh':maosh}
    )
    await message.answer("➕ Qo'shimcha ma'lumotlar")
    await Xodim.next()

@dp.message_handler(state = Xodim.qosh)
async def pul(message:types.Message,state:FSMContext):
    qosh = message.text
    await state.update_data(
        {'qosh':qosh}
    )
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
    await message.answer(f"Xodim kerak:\n\n🏢 Idora: {namei}\n📚 Texnologiya: {texi}\n📥 Telegram: @{user}\n📞 Aloqa: {phone}\n🌐 Hudud: {loc}\n✍️ Mas'ul: {mas_sh}\n🕰 Murojaat vaqti: {time}\n🕰 Ish vaqti: {timei}\n💰 Maosh: {maosh}\n➕ Qo'shimcha: {qosh}")
    await message.answer("Barcha ma'lumotlar to'grimi?",reply_markup=javob)
    await Xodim.next()

#Ustoz kerak
@dp.message_handler(text = 'Ustoz kerak',state='*')
async def ust(message:types.Message):
    await message.answer("Ustoz topish uchun ariza berish\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ism, familiyangizni kiriting?")
    await Ustoz.ism_familiya.set()

@dp.message_handler(state=Ustoz.ism_familiya)
async def ish(message:types.Message,state:FSMContext):
    ism_familiya = message.text
    await state.update_data(
        {"ism_familiya":ism_familiya}
    )
    await message.answer("🕑 Yosh:\nYoshingizni kiriting\nMasalan 16")
    await Ustoz.next()

@dp.message_handler(state=Ustoz.yosh)
async def ag(message:types.Message,state:FSMContext):
    yosh = message.text
    await state.update_data(
        {'yosh':yosh}
    )
    await message.answer("📚  Texnologiya:\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating.\nMasalan Java, C++, C#")
    await Ustoz.next()

@dp.message_handler(state=Ustoz.texno)
async def te(message:types.Message,state:FSMContext):
    texno = message.text
    await state.update_data(
        {'texno':texno}
    )
    await message.answer(f"📞 Aloqa:\nTelefon raqamingizni qoldiring\nMasalan, +998941997111")
    await Ustoz.next()

@dp.message_handler(state=Ustoz.phone)
async def te(message:types.Message,state:FSMContext):
    phone = message.text
    num = "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"
    if re.match(num,phone):
        await state.update_data(
            {'phone':phone}
        )
        await message.answer(f"🌐 Hudud:\nQaysi hududdansiz?\nViloyat nomini,Toshkent shahar yoki Respublikani kiriting.")
        await Ustoz.next()
    else:
        await message.answer("Siz mavjud bo'lmagan raqam kiritdingiz")
        await Ustoz.phone

@dp.message_handler(state=Ustoz.hudud)
async def l(message:types.Message,state:FSMContext):
    hudud = message.text
    await state.update_data(
        {"hudud":hudud}
    )
    await message.answer(f"💰 Narxi:\nTo'lov qilasizmi yoki tekinmi?\nSummani kiriting.")
    await Ustoz.next()

@dp.message_handler(state=Ustoz.narx)
async def l(message:types.Message,state:FSMContext):
    narx = message.text
    await state.update_data(
        {'narx':narx}
    )
    await message.answer(f"👨🏻‍💻 Kasbi:\nO'qiysizmi yoki ishlaysizmi?\nMasalan:Talaba")
    await Ustoz.next()

@dp.message_handler(state=Ustoz.kasb)
async def kas(message:types.Message,state:FSMContext):
    kasb = message.text
    await state.update_data(
        {'kasb':kasb}
    )
    await message.answer(f"🕰 Murojaat qilish vaqti:\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 00:00 - 02:00")
    await Ustoz.next()

@dp.message_handler(state=Ustoz.vaqt)
async def vt(message:types.Message,state:FSMContext):
    vaqt = message.text
    await state.update_data(
        {'vaqt':vaqt}
    )
    await message.answer(f"🔎 Maqsad:\nMaqsadingizni qisqacha yozing")
    await Ustoz.next()

@dp.message_handler(state=Ustoz.maqsad)
async def vt(message:types.Message,state:FSMContext):
    maqsad1 = message.text
    await state.update_data(
        {'maqsad':maqsad1}
    )
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
    await message.answer(f"Ustoz kerak:\n\n👨‍💻 Shogird: {fname}\n🌐 Yosh: {age}\n📚 Texnologiya: {techno}\n📥 Telegram: @{user}\n📞 Aloqa: {phone}\n🌐 Hudud: {loc}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {prof}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}")
    await message.answer("Barcha ma'lumotlar to'grimi?",reply_markup=javob)
    await  Ustoz.next()

#Shogird
@dp.message_handler(text = 'Shogird kerak',state='*')
async def shog(message:types.Message):
    await message.answer("Shogird topish uchun ariza berish\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ism, familiyangizni kiriting?")
    await Shogird.ism.set()
@dp.message_handler(state= Shogird.ism)
async def ismf(message:types.Message,state:FSMContext):
    ism = message.text
    await state.update_data(
        {'ism': ism}
    )
    await message.answer("🕑 Yosh:\nYoshingizni kiriting\nMasalan 16")
    await Shogird.next()

@dp.message_handler(state=Shogird.yosh)
async def agsh(message:types.Message,state:FSMContext):
    yosh = message.text
    state.update_data(
        {'yosh':yosh}
    )
    await message.answer(f"📚 Texnologiya:\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating.\nMasalan: Java, C++, C#")
    await Shogird.next()

@dp.message_handler(state = Shogird.texno)
async def texno(message:types.Message,state:FSMContext):
    texno = message.text
    await state.update_data(
        {'texno': texno}
    )
    await message.answer(f"📞 Aloqa:\nTelefon raqamingizni qoldiring\nMasalan, +998941997111")
    await Shogird.next()

@dp.message_handler(state=Shogird.phone)
async def get_p(message:types.Message,state:FSMContext):
    phone = message.text
    num = "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"
    if re.match(num,phone):
        await state.update_data(
            {'phone':phone}
        )
        await message.answer(f"🌐 Hudud:\nQaysi hududdansiz?\nViloyat nomini,Toshkent shahar yoki Respublikani kiriting.")
        await Shogird.next()
    else:
        await message.answer("Siz mavjud bo'lmagan raqam kiritdingiz")
        await Shogird.phone


@dp.message_handler(state=Shogird.hudud)
async def get_l(message:types.Message,state:FSMContext):
    hudud1 = message.text
    await state.update_data(
        {'hudud': hudud1}
    )
    await message.answer(f"💰 Narxi:\nTo'lov qilasizmi yoki tekinmi?\nSummani kiriting.")
    await Shogird.next()

@dp.message_handler(state=Shogird.narx)
async def get_p(message:types.Message,state:FSMContext):
    narx = message.text
    await state.update_data(
        {'narx': narx}
    )
    await message.answer(f"👨🏻‍💻 Kasbi:\nO'qiysizmi yoki ishlaysizmi?\nMasalan:Talaba")
    await Shogird.next()
@dp.message_handler(state=Shogird.kasb)
async def ask_kasb(message:types.Message,state:FSMContext):
    kasb = message.text
    await state.update_data(
        {'kasb': kasb}
    )
    await message.answer(f"🕰 Murojaat qilish vaqti:\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 00:00 - 02:00")
    await Shogird.next()
@dp.message_handler(state=Shogird.vaqt)
async def ask_vaqt(message:types.Message,state:FSMContext):
    vaqt1 = message.text
    await state.update_data(
        {'vaqt': vaqt1}
    )
    await message.answer(f"🔎 Maqsad:\nMaqsadingizni qisqacha yozing")
    await Shogird.next()
@dp.message_handler(state=Shogird.maqsad)
async def ask_m(message:types.Message,state:FSMContext):
    maqsad2 = message.text
    await state.update_data(
        {'maqsad':maqsad2}
    )
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
    await message.answer(f"Shogird kerak:\n\n🎓 Ustoz: {full}\n🌐 Yosh: {age}\n📚 Texnologiya: {texno}\n📥 Telegram: @{user}\n📞 Aloqa: {phne}\n🌐 Hudud: {mnl}\n💰 Narxi: {price}\n👨🏻‍💻 Kasbi: {ksb}\n🕰 Murojaat qilish vaqti: {time}\n🔎 Maqsad: {goal}")
    await message.answer("Barcha ma'lumotlar to'grimi?",reply_markup=javob)
    await Shogird.next()




if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)