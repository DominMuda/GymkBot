# encoding :utf-8
from datetime import date, datetime
from subprocess import call
import telebot, os.path
import logging
import configparser
import io


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

pruebas_disponibles = []
bool_list = []
for x in range(0,10):
	bool_list.insert(x,False)
	pruebas_disponibles.insert(x, "/prueba" + str(x + 1))

config = configparser.ConfigParser()
config.read("config.ini")

token = config['Bot']['token']
admin_id = config['Admin']['chat_id']
bot = telebot.TeleBot(token, skip_pending=True)

def create_DB():
	self.conn = sqlite3.connect(dbName)
	c = self.conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS userTable(userId INTEGER NOT NULL UNIQUE, userName TEXT NOT NULL, chatID TEXT)')

def main():

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
		tmp_list = ""
		for x in range(0,10):
			tmp_list += "\n - " + str(pruebas_disponibles[x])
		reply = "Los comandos que puedes usar son: \n" + tmp_list
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /help\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
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

		@bot.message_handler(commands=['prueba1'])
		def send_help(message):
			reply = "De momento, no has cumplimentado ninguna prueba: \n"
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
			f.writelines("[%s/%s/%s - %s:%s:%s] \n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) + " El usuario "+ user + " ha enviado una foto.\n" )
			f.close

			raw = m.photo[-1].file_id
			file_info = bot.get_file(raw)
			downloaded_file = bot.download_file(file_info.file_path)
			thing = io.BytesIO(downloaded_file)
			thing.name = raw + "png"
			bot.send_photo(admin_id, thing)

	@bot.message_handler(content_types=['voice'])
	def audio(*mensaje):
		for m in mensaje:
			chat_id = m.chat.id
			user = m.chat.username
			nombreChat = m.chat.first_name

			f = open('log','a')
			now = datetime.now()
			f.writelines("***************\n")
			f.writelines("[%s/%s/%s - %s:%s:%s] \n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) + " El usuario "+ user + " ha enviado un audio.\n" )
			f.close

			raw = m.voice.file_id
			file_info = bot.get_file(raw)
			downloaded_file = bot.download_file(file_info.file_path)
			thing = io.BytesIO(downloaded_file)
			thing.name = raw + "ogg"
			bot.send_voice(admin_id, thing)

	@bot.message_handler(func=lambda m: True)
	def save_on_log(message):
		f = open('log','a')
		now = datetime.now()
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + message.text + "\n")
		f.close

	bot.polling()

if __name__ == "__main__":
	main()
