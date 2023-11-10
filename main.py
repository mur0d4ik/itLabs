from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from buttons import *
from config import *
from state import *

storage = MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
state = FSMContext

UserInfo = {}

################################## Команды ##################################



@dp.message_handler(commands = 'start')
async def welcomeUser(message: types.Message):

    UserInfo["ID"] = message.from_user.id

    await message.answer("Tanglang", reply_markup = await menuFunc())

    print(UserInfo["ID"])



##################################



@dp.message_handler(commands = 'help')
async def CMhelp(message: types.Message):

    await message.answer("""Buyruqlar: 
/start - Botni ishga tushirish
/help - Yordam""")
    


##################################



@dp.message_handler(commands = 'obunachilar_soni')
async def CMusers(message: types.Message):

    await message.answer("Botimizda 1081 ta obunachi mavjud")



#############################################################################





#############################################################################



@dp.callback_query_handler(text = "oquvMarkaz")
async def mainFunc(call: types.CallbackQuery):
    await call.message.answer(mainMenuInfo[call.data], reply_markup = await locFUNC())
    await call.message.delete()



################################## Вывод всех Курсов



@dp.callback_query_handler(text = "bizningKurslar")
async def mainFunc(call: types.CallbackQuery):
    await call.message.answer_photo(

        photo = open("img/branches.jpg", "rb"),
        caption = mainMenuInfo["bizningKurslar"], reply_markup = await CoursesFUNC())
    
    await call.message.delete()



################################## Вывод номера Компании



@dp.callback_query_handler(text = "bizBB")
async def mainFunc(call: types.CallbackQuery):
    await call.message.answer(mainMenuInfo[call.data], reply_markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text = "⬅️Ortga", callback_data = "backContact")))
    await call.message.delete()



################################## Отправка локацияи Чилазар



@dp.callback_query_handler(text = "chilonzorF")
async def locFunc(call: types.CallbackQuery):
    await bot.send_location(call.message.chat.id, CenterLoc[call.data][0], CenterLoc["chilonzorF"][1], reply_markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text = "Ortga", callback_data = "backLOC")))
    await call.message.delete()



################################## Отправка локацияи Беруний 



@dp.callback_query_handler(text = "beruniyF")
async def locFunc(call: types.CallbackQuery):
    await bot.send_location(call.message.chat.id, CenterLoc[call.data][0], CenterLoc["chilonzorF"][1], reply_markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text = "Ortga", callback_data = "backLOC")))
    await call.message.delete()



################################## STATE начало



@dp.callback_query_handler(text = "kursgaYozilish")
async def locFunc(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Ismingizni kiriting!")
    await User.name.set()



##################################



@dp.callback_query_handler(state = User.name)
async def locFunc(call: types.CallbackQuery, state: FSMContext):

    nameUser = call.message.text
    await state.update_data(name = nameUser)

    await call.message.answer("Yoshingizni kiriting!")
    await User.age.set()



##################################



@dp.callback_query_handler(state = User.age)
async def locFunc(call: types.CallbackQuery, state: FSMContext):

    ageUser = call.message.text
    await state.update_data(age = ageUser)

    await call.message.answer("Kursni tanglang!", reply_markup = await coursesFUNC())
    await User.course.set()



##################################



@dp.callback_query_handler(state = User.course)
async def locFunc(call: types.CallbackQuery, state: FSMContext):

    courseUser = call.message.text
    await state.update_data(course = courseUser)

    await call.message.answer("Kursni tanglang!")
    await User.course.set()



################################## Назад из меню ЛОКАЦИЯ



@dp.callback_query_handler(text = "backLOC")
async def backFunc(call: types.CallbackQuery):
    await call.message.answer(mainMenuInfo["oquvMarkaz"], reply_markup = await locFUNC())
    await call.message.delete()



################################## Назад из меню номера Компании



@dp.callback_query_handler(text = "backContact")
async def backFunc(call: types.CallbackQuery):
    await call.message.answer("Tanglang", reply_markup = await menuFunc())
    await call.message.delete()



################################## Назад из меню контретного Курса 



@dp.callback_query_handler(text = "coursesBack")
async def backFunc(call: types.CallbackQuery):
    await call.message.answer_photo(

        photo = open("img/branches.jpg", "rb"),
        caption = mainMenuInfo["bizningKurslar"], reply_markup = await CoursesFUNC())
    
    await call.message.delete()



################################## Назад из меню Курсов в Основное меню



@dp.callback_query_handler(text = "backCourses")
async def backFunc(call: types.CallbackQuery):
    await call.message.answer(mainMenuInfo["bizningKurslar"], reply_markup = await menuFunc())
    await call.message.delete()



################################## Выход из конткретной Локации




@dp.callback_query_handler(text = "backLOC")
async def backFunc(call: types.CallbackQuery):
    await call.message.answer(mainMenuInfo["oquvMarkaz"], reply_markup = await locFUNC())
    await call.message.delete()



################################## Выход из меню Локации



@dp.callback_query_handler(text = "backCenter")
async def backFunc(call: types.CallbackQuery):
    await call.message.answer(mainMenuInfo["oquvMarkaz"], reply_markup = await menuFunc())
    await call.message.delete()



################################## Вывод Курсов



@dp.callback_query_handler()
async def CousesM(call: types.CallbackQuery):

    await call.message.answer_photo(

        photo = open(f"img/{call.data}.jpg", "rb"),
        caption = coursesInfo[call.data], reply_markup = coursesInfoButton

    )

    await call.message.delete()
    

















if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)