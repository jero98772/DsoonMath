
from DsoonMath import quantity ,answertime,answer, p,error 
from exercises import mix 
import time
#@Ds00nMathbot
import telebot
token = ""

bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True)
def dailyquest(message):	 

	chat_id = message.chat.id
	while True:
		expresion = mix()
		answer_ = answer(expresion)
		print("answer",answer_,"expresion",expresion)
		bot.send_message(chat_id =chat_id ,text = "hi this is the problem \n"+str(expresion)+"\nplease wait the answer")
		time.sleep(30)
		bot.send_message(chat_id =chat_id ,text = str(expresion+" answer:==>\n"+str(answer_)))	

bot.polling()

