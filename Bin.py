import telebot

# استبدال "TOKEN" بتوكن البوت الخاص بك
bot = telebot.TeleBot("6595541927:AAGNKnX2qT_HFn-l0aN2UpydTbCqWWNFbyE")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # استخراج النص من الرسالة المستلمة
    text = message.text

    # افتح ملف نصي جديد للكتابة
    with open("text_file.txt", "w") as file:
        # اكتب النص في الملف
        file.write(text)

    # أرسل الملف النصي للمستخدم
    with open("text_file.txt", "rb") as file:
        bot.send_document(message.chat.id, file)

    # أرسل رسالة تأكيد للمستخدم
    bot.reply_to(message, "تم تحويل الرسالة إلى ملف نصي وإرساله!")

# ابدأ استقبال التحديثات
bot.polling()
