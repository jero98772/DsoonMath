
from DsoonMath import quantity ,answertime,answer
from flask import Flask
import time
import telebot
API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)
while True:
	limit = 999
	level = 2
	expresion = quantity(levelop= level,leveDt=level-1,limt=limit)
	bot.send_message(chat_id = "",text = str(expresion))
	time.sleep(60*60*24)






