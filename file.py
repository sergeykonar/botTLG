import telebot


token = "918993617:AAELPpt_-TlM8oRYR2jg4MovCEVgHPeVFfk"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def handle_text(message):
	bot.send_message(message.chat.id, "UKR | Привіт. Цей бот призначений для створення поста у https://t.me/srch_uzh. \n Правила користування: \n 1) Писати текст одним повідомленням \n 2) До текста можна приєднати одну фотографію \n 3) Усі пости анонімні. Якщо хочете зробити свій пост не анонімним, то просто напишіть свій нікнейм в Telegram через @, наприклад, @srch_uzh\n \n \n \n RUS | Привет. Этот бот предназначен для создания поста в https://t.me/srch_uzh. \n Правила использования: \n 1) Писать текст одним сообщением \n 2) К тексту можно присоеденить одну фотографию \n 3) Все посты анонимны. Если хотите сделать свой пост не анонимным, то просто напишите свой никнейм в Telegram ерез @, например, @srch_uzh")
	
@bot.message_handler(func=lambda message: True, content_types=['photo', 'text'])

def echo_all(message):
	upd = bot.get_updates()
	last_upd = upd[-1]
	message_from_user = last_upd.message
	#print(message_from_user.message_id)
	msg = message_from_user.message_id
	idFrom = message_from_user.chat.id
	bot.forward_message(355654520, idFrom, msg)
	bot.send_message(message.chat.id, "UKR | Ваше повідомлення отримано! Очікуйте публікації! \n \n RUS | Ваше сообщение получено! Ожидайте публикации!")


bot.polling(none_stop=True, interval=3)	