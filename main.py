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



@dp.message_handler(state = User.name)
async def locFunc(message: types.Message, state: FSMContext):

    nameUser = message.text
    await state.update_data(name = nameUser)

    await message.answer("Yoshingizni kiriting!")
    await User.age.set()



##################################



@dp.message_handler(state = User.age)
async def locFunc(message: types.Message, state: FSMContext):

    ageUser = message.text

    if ageUser.isdigit():
        await state.update_data(age = ageUser)

        await message.answer("Kursni tanglang!", reply_markup = await coursesFUNC())
        await User.course.set()

    else:
        await message.answer("❌Yoshingizni sonlarda kiriting!")



##################################



@dp.message_handler(state = User.course)
async def locFunc(message: types.Message, state: FSMContext):

    courseUser = message.text
    await state.update_data(course = courseUser)
     
    await message.answer("Nomeringizni yuboring!", reply_markup = contact)
    await User.phone_number.set()



##################################



@dp.message_handler(content_types = "contact" ,state = User.phone_number)
async def locFunc(message: types.Message, state: FSMContext):
        
        phoneNumber = message.contact['phone_number']
        await state.update_data(phone_number = phoneNumber)

        await message.answer("...", reply_markup = types.ReplyKeyboardRemove())
        
        data = await state.get_data()
        Name = data.get("name")
        Age = data.get("age")
        Course = data.get("course")
        PhoneNumber = data.get("phone_number")

        
        info = f"""☑️ Sizning ma'lumotlaringiz!

📄 F.I.O: - {Name}
👤 Yosh: {Age}
🖥 Kurs: {Course}
📞 Telefon: {PhoneNumber}

⚠️ Ma'lumotlaringiz to'g'rimi?"""
        
        await message.answer_photo(
            photo = open("img/userInfo.jpg", "rb"),
            caption = info, reply_markup = await ChooseFUNC()
            )
        
        await User.choose.set()



@dp.callback_query_handler(text = "true", state = User.choose)
async def choose(call: types.CallbackQuery, state: FSMContext):

    ChooseUser = call.data
    await state.update_data(choose = ChooseUser)

    data = await state.get_data()
    Name = data.get("name")
    Age = data.get("age")
    Course = data.get("course")
    PhoneNumber = data.get("phone_number")
    
    Info = f"""✅ Quyidagi ma'lumotlar qabul qilindi!

📄 F.I.O: - {Name}
👤 Yosh: {Age}
🖥 Kurs: {Course}
📞 Telefon: {PhoneNumber}"""

    await bot.send_message(chat_id = 809673082, text = Info)
    await call.message.delete()

    await User.choose.set()



@dp.callback_query_handler(text = "false", state = User.choose)
async def choose(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    ChooseUser = call.data
    await state.update_data(choose = ChooseUser)

    await state.finish()
    await state.reset_data()

    await call.message.answer("Ma'lumotlaringiz o'chirildi🔥", reply_markup = await menuFunc())



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