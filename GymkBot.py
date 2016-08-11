# encoding :utf-8
from datetime import date, datetime
from subprocess import call
import telebot, os.path
import logging
import configparser
import io,sys
import sqlite3


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

pruebas_disponibles = []
bool_list = []
for x in range(0,40):
	bool_list.insert(x,False)
	pruebas_disponibles.insert(x, "/prueba" + str(x + 1))

config = configparser.ConfigParser()
config.read("config.ini")

token = config['Bot']['token']
admin_id = config['Admin']['chat_id']
bot = telebot.TeleBot(token, skip_pending=True)
dbName = config['DataBase']['db_name']
conn = sqlite3.connect(dbName)


def addUser(message):
	try:
		print ('hello1\n')
		conn = sqlite3.connect(dbName)
		c = conn.cursor()
		print ('hello2\n')
		deId = message.chat.id
		username = message.chat.username
		first_name = message.chat.first_name
		print (str(deId)  + username + first_name)
		c.execute('INSERT or REPLACE INTO userTable VALUES(?, ?, ?)', (str(deId), username, first_name))
		print ('usuario introducido con exito\n')
		conn.commit()
		return True
	except:
		print('\nErrors in addUser: ' + str(sys.exc_info()[0]))
		return False
	else:
		return expenseID

def getUsers():
	try:
		conn = sqlite3.connect(dbName)
		c = conn.cursor()
		h = c.execute('SELECT userName FROM userTable')
		conn.commit()
		print ('hello\n')
		return h
	except:
		print('\nErrors in getUsers: ' + str(sys.exc_info()[0]))
		return False
	else:
		return expenseID

def create_DB():
	c = conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS userTable(userId TEXT NOT NULL UNIQUE, userName TEXT NOT NULL, firstName TEXT)')
	conn.commit()
	conn.close()
	return True

def main():

	create_DB()

	@bot.message_handler(commands=['start'])
	def send_welcome(message):
		pruebas = ''
		for x in range (0,40):
	 		pruebas += "0"
		addUser(message)
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

	@bot.message_handler(commands=['users'])
	def send_rules(message):
		h = getUsers()
		f = open('log', 'a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /reglas\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second)+ message.chat.username + " ha solicitado las relgas.\n")
		f.close
		for row in h:
			bot.send_message(message.chat.id, row)


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
		reply = "__ __ __ __ __ __ __ __\n"
		f = open('log','a')
		now = datetime.now()
		f.writelines("***************\n")
		f.writelines("[%s/%s/%s - %s:%s:%s] /progreso	\n" % (now.day, now.month, now.year, now.hour, now.minute, now.second) )
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
				reply = (message.chat.username + " ha intentado desbloquear las pruebas. \n")
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
		f.writelines("[%s/%s/%s - %s:%s:%s] "  % (now.day, now.month, now.year, now.hour, now.minute, now.second) + message.chat.first_name + " dijo: " + message.text + "\n")
		f.close

	bot.polling()

if __name__ == "__main__":
	main()
