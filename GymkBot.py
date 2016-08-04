# encoding :utf-8
from datetime import date, datetime
from subprocess import call
import telebot, os.path
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
import logging
import io


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

updater = Updater(token='269890633:AAHaYy-FkcZwm1ooxtMmfTJ3yIhjbnfNe2E')
bool_list = [False,False,False,False,False,False,False,False,False,False]

dispatcher = updater.dispatcher

def main():

	bot = telebot.TeleBot('269890633:AAHaYy-FkcZwm1ooxtMmfTJ3yIhjbnfNe2E', skip_pending=True)
	pruebas_disponibles = []

	@bot.message_handler(commands=['start'])
	def send_welcome(message):
		reply = "Bot para realizar una encuesta.\nPara conocer los detalles de cada prueba escribe /help"
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /start\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + reply + "\n")
		f.close
		bot.reply_to(message, reply)

	@bot.message_handler(commands=['help'])
	def send_help(message):
		reply = "Los comandos que puedes usar son: \n - \n - \n -"
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /start\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + reply + "\n")
		f.close
		bot.send_message(message.chat.id, reply)

	@bot.message_handler(commands=['progreso'])
	def send_help(message):
		reply = "De momento, no has cumplimentado ninguna prueba: \n"
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /start\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + reply + "\n")
		f.close
		bot.send_message(message.chat.id, reply)

	@bot.message_handler(content_types=['photo'])
	def photo(*mensaje):
		for m in mensaje:
			chat_id = m.chat.id
			user = m.chat.username
			nombreChat = m.chat.first_name

			f = open('log','a')
			now = datetime.now()
			f.writelines("***************\n")
			f.writelines("[%s/%s/%s - %s:%s:%s] \n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) + " El usuario "+ user + " ha enviado una foto." )
			f.close

			raw = m.photo[-1].file_id
			file_info = bot.get_file(raw)
			downloaded_file = bot.download_file(file_info.file_path)
			thing = io.BytesIO(downloaded_file)
			thing.name = raw + "png"
			bot.send_photo("57311471", thing)

	@bot.message_handler(content_types=['audio'])
	def audio(*mensaje):
		for m in mensaje:
			chat_id = m.chat.id
			user = m.chat.username
			nombreChat = m.chat.first_name

			f = open('log','a')
			now = datetime.now()
			f.writelines("***************\n")
			f.writelines("[%s/%s/%s - %s:%s:%s] \n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) + " El usuario "+ user + " ha enviado un audio." )
			f.close

			raw = m.audio[-1].file_id
			file_info = bot.get_file(raw)
			downloaded_file = bot.download_file(file_info.file_path)
			thing = io.BytesIO(downloaded_file)
			thing.name = raw + "mp3"
			bot.send_photo("57311471", thing)


	@bot.message_handler(func=lambda m: True)
	def save_on_log(message):
		f = open('log','a')
		now = datetime.now()
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + message.text + "\n")
		f.close

	bot.polling()

if __name__ == "__main__":
	main()
