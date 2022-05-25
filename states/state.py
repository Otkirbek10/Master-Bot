
from aiogram.dispatcher.filters.state import State,StatesGroup

class Sherik(StatesGroup):
    ism_familiya = State()
    texno = State()
    phone = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()
    send = State()

class Ish(StatesGroup):
    xodim = State()
    yosh = State()
    texno = State()
    phone = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()
    send = State()

class Xodim(StatesGroup):
    idora = State()
    texno = State()
    phone = State()
    hudud = State()
    masul = State()
    vaqt = State()
    ivaqt = State()
    maosh = State()
    qosh = State()
    send = State()

class Ustoz(StatesGroup):
    ism_familiya = State()
    yosh = State()
    texno = State()
    phone = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()
    send = State()

class Shogird(StatesGroup):
    ism = State()
    yosh = State()
    texno = State()
    phone = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()
    send = State()

