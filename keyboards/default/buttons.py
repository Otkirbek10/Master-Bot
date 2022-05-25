from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'Sherik kerak'),KeyboardButton(text  = 'Ish joyi kerak')],
        [KeyboardButton(text = 'Xodim kerak'), KeyboardButton(text = 'Ustoz kerak')],
        [KeyboardButton(text = 'Shogird kerak')]
        

    ],
    resize_keyboard=True,
    one_time_keyboard=True

)

javob = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='HA✅'),KeyboardButton(text='YO\'Q❌')]
    ],
    resize_keyboard=True
)

contactnum = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni ulashish", request_contact=True)
        ]
    ],
    resize_keyboard=True
) 

