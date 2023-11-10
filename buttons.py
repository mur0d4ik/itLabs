from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


###############################################################################


mainMenu = {

    "🏢O'quv marakz" : "oquvMarkaz",
    "🗂Bizning kurslar" : "bizningKurslar",
    "📞Biz bilan bog'lanish" : "bizBB",
    "📝Kursga yozilish" : "kursgaYozilish"

}



##################################



mainMenuInfo = {

    "oquvMarkaz" : "Bizning fillialarimiz!",
    "bizningKurslar" : "Bizning kurslar",
    "bizBB" : "Qo'shimcha savol va takliflar uchun\ntel: +998981219808",
    "kursgaYozilish" : "FUNC"

}



##################################



Center = {

    "🏢Chilonzor filliali" :"chilonzorF",
    "🏢Beruniy filliali" : "beruniyF",
    "⬅️Ortga" : "backCenter"
}



##################################



async def locFUNC():
    buttons = InlineKeyboardMarkup()

    for key, value in Center.items():
        buttons.add(InlineKeyboardButton(text = key, callback_data = value))

    return buttons



##################################



CenterLoc = {

    "chilonzorF" : [41.2893439, 69.2211981],
    "beruniyF" : [41.3414431, 69.2047115]

}



##################################



Courses = {

    "📱Android dasturlash" : "android",
    "💻Backend dasturlash" : "backend",
    "🖥Fronted dasturlash" : "fronted",
    "🎯SMM kurslar" : "smm",
    "👨‍🎨Design" : "design",
    "📝Kursga yozilish" : "kursgaYozilish",
    "⬅️Ortga" : "backCourses"

}



##################################



async def CoursesFUNC():

    buttons = InlineKeyboardMarkup()

    for key, value in Courses.items():
        buttons.add(InlineKeyboardButton(text = key, callback_data = value))

    return buttons



##################################



coursesInfo = {



    "android" : """📱Mobile App Development (Flutter): 

 ⏰ Dars vaqti: 90 daqiqa

 📅 Kurs davomiyligi 6 oy

 💸 Kurs narxi oyiga 599 ming so'm.


Kursda nimalarni o'rganasiz?: 


🟢 Dasturlash asoslari
🟢 Dart bilan ishlash
🟢 Algoritimlar 
🟢 Flutter bilan ishlash
🟢 Mobil dastur yaratish
🟢 Play matketga joylash

📌Kurs davomida shaxsiy portfoilo yaratasiz. 

🚀Darslarda 100% amaliy bilimlarga ega bo'lasiz.""",



    "backend" : """🐍 Python dasturlash kursi haqida...  


⏰  Kurs vaqtlari  14:00 dan 15:30,
         15:30 dan 17:00 gacha bo'ladi.

📅  Kurs 6 oylik, haftasiga 3 kun 
         (toq yoki juft kunlari)

 🔥Kurs narhi oyiga 599 ming so'm.🔥
 
Kursda ko'plab qiziqarli loyihalar, marafonlar bo'lib o'tadi. 

Nimalarni o‘rgatamiz ?:

✅ Dasturlash asoslari
✅ Python bilan ishlash
✅ Ma'lumotlar bazasi(Sqlite,Postgres)
✅ Telegram Bot 
✅ Django Framework
✅ REST API 
✅ Web loyiha yaratish
✅ Git""",



    "fronted" : """🖥 Front-End Web dasturlash: 

 ⏰ Dars vaqti: 90 daqiqa

 📅 Kurs davomiyligi 6 oy

 💸 Kurs narxi oyiga 599 ming so'm.


Kursda nimalarni o'rganasiz?: 


🔸 -HTML5
🔸 -CCS3
🔸 -Sass
🔸 -Bootstrap 5
🔸 -Git
🔸 -Github
🔸 -JavaScript
🔸 -VueJS
🔸 -Photoshop
🔸 -Figma
🔸 -BEM metodologiyasi

📌Kurs davomida shaxsiy portfoilo yaratasiz. 

🚀Darslarda 100% amaliy bilimlarga ega bo'lasiz.""",



    "smm" : """🎯 SMM (Social Media Marketing): 

 ⏰ Dars vaqti: 90 daqiqa.

 📅 Kurs davomiyligi 2 oy, haftasiga 2 marttadan. 

 💸 Kurs narxi oyiga 599 ming so'm.

 🎯 "SMM mutaxassisi" kursini tamomlab, siz Digital marketingning asosiy online yo'nalishi hisoblangan daromadli💰 eng asosiysi rivojlanib borayotgan kasbni egasiga aylanasiz.


Nimalarni o‘rgatamiz:

🔸 - SMM asoslari;
🔸 - Internet marketing;
🔸 - Maqsadli auditoriya tanlash;
🔸 - Ijitimoiy tarmoqlar bilan ishlash (Instagram, Facebook, Telegram, TikTok);
🔸 - Target ( Reklama sozlamalari);
🔸 - SMM post dizayn asoslari;
🔸 - Kontent tuzish;
🔸 - Mijozlarga internet tarmoqlarida to'g'ri javob berishni o'rgatamiz;
🔸 - Statistika ma'lumotlari bilan ishlash;
🔸 - Copyrighting asoslari;
🔸 - Video roliklarni tahrirlashni o'rgatamiz;
🔸 - Bir necha foydali servislar bilan ishlash


📌Kurs davomida shaxsiy portfoilo yaratasiz. 

🚀Darslarda 70% amaliy 30% nazariy bilimlarga ega bo'lasiz.""",



    "design" : """👨‍🎨Design 2.0 (Graphic,Polygraphic, Web Design): 

 ⏰ Dars vaqti: 90 daqiqa

 📅 Kurs davomiyligi 4oy

 💸 Kurs narxi oyiga 799ming so'm.


Kursda nimalarni o'rganasiz?: 


🟢 Adobe Photoshop
🟢 Adobe Illustrator
🟢 Figma
🟢Praktika

📌Kurs davomida shaxsiy portfoilo yaratasiz. 

🚀Darslarda 100% amaliy bilimlarga ega bo'lasiz."""



}



##################################



coursesInfoButton = InlineKeyboardMarkup().add(InlineKeyboardButton(text = "⬅️Ortga", callback_data = "coursesBack"))



##################################



async def menuFunc():

    mainMenuButtons = InlineKeyboardMarkup(row_width = 2)

    for key, value in mainMenu.items():
        mainMenuButtons.insert(InlineKeyboardButton(text = key, callback_data = value))

    return mainMenuButtons



###############################################################################



coursesState = ["📱Flutter", "🐍Python", "🖥Fronted", "🎯SMM", "👨‍🎨Design"]



async def coursesFUNC():

    buttons = ReplyKeyboardMarkup(resize_keyboard = True)

    for i in coursesState:
        buttons.add(text = i)

    return buttons



###############################################################################





###############################################################################