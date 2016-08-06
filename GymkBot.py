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
		reply = "Los comandos que puedes usar son: \n" + tmp_list + "\nSi necesitas saber las reglas de la gymkana, pulsa en /reglas"
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /help\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + reply + "\n")
		f.close
		bot.send_message(message.chat.id, reply)

	@bot.message_handler(commands=['reglas'])
	def send_rules(message):
		tmp_list = ""
		for x in range(0,10):
			tmp_list += "\n - " + str(pruebas_disponibles[x])
		h = open('Reglas_de_la_Gymkana','r')
		f = open('log', 'a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /reglas\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second)+ message.chat.username + " ha solicitado las relgas.\n")
		f.close
		bot.send_document(message.chat.id, h)

	@bot.message_handler(commands=['progreso'])
	def send_progress(message):
		reply = "De momento, no has cumplimentado ninguna prueba: \n"
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /start\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + reply + "\n")
		f.close
		bot.send_message(message.chat.id, reply)

	@bot.message_handler(commands=['prueba1'])
	def send_game1(message):
		reply = "Me alegra que hayas empezado a jugar! La primera prueba es simple. Será que envies la imagen que quieras \n"
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /prueba1\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + reply + "\n")
		f.close
		bot.send_message(message.chat.id, reply)

	@bot.message_handler(commands=['unlock'])
	def send_progress(message):
		index = message.text.split(' ')
		print ("\n\n"+  message.text.lower() + str(len(index)) + "\n")
		if not len(index) == 2 or not index[1].isnumeric() or int(index[1]) < 1 or int(index[1]) > 10:
			reply = "No has introducido los datos correctamente"
		else:
			if message.chat.id == admin_id:
				reply = ("Desbloqueando la prueba " + index[1] + ". \n")
			else:
				reply = (message.chat.username + " ha intentado desbloquear las pruebas. \n"
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /unlock\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + reply + "\n")
		f.close
		bot.reply_to(message, reply)

	def send_admin(header, raw):
		file_info = bot.get_file(raw)
		downloaded_file = bot.download_file(file_info.file_path)
		thing = io.BytesIO(downloaded_file)
		thing.name = raw + header
		if header == "png":
			bot.send_photo(admin_id, thing)
		elif header == "ogg":
			bot.send_voice(admin_id, thing)

	@bot.message_handler(content_types=['photo'])
	def photo(*mensaje):
		for m in mensaje:
			chat_id = m.chat.id
			user = m.chat.username
			nombreChat = m.chat.first_name
			raw = m.photo[-1].file_id

			f = open('log','a')
			now = datetime.now()
			f.writelines("***************\n")
			f.writelines("[%s/%s/%s - %s:%s:%s] \n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) + " El usuario "+ user + " ha enviado una foto.\n" )
			f.close

			send_admin("png", raw )

	@bot.message_handler(content_types=['voice'])
	def audio(*mensaje):
		for m in mensaje:
			chat_id = m.chat.id
			user = m.chat.username
			nombreChat = m.chat.first_name
			raw = m.voice.file_id

			f = open('log','a')
			now = datetime.now()
			f.writelines("***************\n")
			f.writelines("[%s/%s/%s - %s:%s:%s] \n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) + " El usuario "+ user + " ha enviado un audio.\n" )
			f.close

			send_admin("ogg", raw)

	@bot.message_handler(func = lambda m: True)
	def save_on_log(message):
		f = open('log','a')
		now = datetime.now()
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + message.chat.username + " dijo: " + message.text + "\n")
		f.close

	bot.polling()

if __name__ == "__main__":
	main()
