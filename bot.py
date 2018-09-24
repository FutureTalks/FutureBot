# -*- coding: utf-8 -*-
import sys
import traceback
import logging
import telepot
from telepot.delegate import per_from_id, per_chat_id, per_inline_from_id, create_open, pave_event_space, include_callback_query_chat_id
from telepot.namedtuple import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from SQLight import SQLight
import urllib2

#Other files
import config
import customConfig
import adminHandler
import userHandler
import AWSHandler


"""
FutureBot, the collaborative bot project

"""

class FutureBot(telepot.helper.ChatHandler):

	def __init__(self, *args, **kwargs):
		super(FutureBot, self).__init__(*args, **kwargs)
		self._state = 0
		

	# Handle messages
	def on_chat_message(self, msg):
		# ID from chat
		content_type, chat_type, chat_id = telepot.glance(msg, flavor='chat')
		print(content_type)
		print(chat_type)
		print(chat_id)

		if content_type == 'text':
			print("Message")
			msgText = msg.get('text', '')
			self.handleText(msg, chat_id, msgText)
			
		if content_type == 'photo':
			print("Image")
			msgData = msg['photo'][len(msg['photo'])-1]['file_id']
			filepath = bot.getFile(msgData)['file_path']
			fullpath = 'https://api.telegram.org/file/bot'+customConfig.token+'/'+filepath
			content = urllib2.urlopen(fullpath).read()
			#print(fullpath)
			self.handleImage(content, chat_id)
			

	# Handle callback querys
	def on_callback_query(self, msg):
		print("Callback")
		query_id, chat_id, data = telepot.glance(msg, flavor='callback_query')
		self.handleText(msg, chat_id, msg['data'])


	def handleImage(self, content, chat_id):
		try:
			AWSHandler.handleImage(content, chat_id, bot)

		except Exception as e:
			# Error with traceback
			trace = traceback.format_exc()
			errMessage = unicode(trace) + unicode(str(e))
			print (str(errMessage))
			bot.sendMessage(chat_id, errMessage)


	# Handle text-message here -------------------------------------------------------------
	def handleText(self, msg, chat_id, text):
		try:
			#Check if admin
			isAdmin = chat_id in customConfig.admins
			if isAdmin:
				self.handleAdmin(text, msg, chat_id)  

			#Handle normal users
			self.handleUser(text, msg, chat_id)

			#Handle Cloud commands with text
			AWSHandler.handleText(text, msg, chat_id, bot)


		except Exception as e:
			# Error with traceback
			trace = traceback.format_exc()
			errMessage = unicode(trace) + unicode(str(e))
			print (str(errMessage))
			bot.sendMessage(chat_id, errMessage)


	#ADMIN ---------------------------------------------------------------------------
	def handleAdmin(self, command, msg, chat_id):
		print (unicode('ADMIN MODE:-------- '))
		adminHandler.handleAdmin(command, msg, chat_id, bot)
		

	#NORMAL USER ------------------------------------------------------------------------
	def handleUser(self, command, msg, chat_id):
		userHandler.handleUser(command, msg, chat_id, bot)
		




# Runs once -----------------------------------------------------------------------------------------------------------

# Initialize bot
bot = telepot.DelegatorBot(customConfig.token,[
	include_callback_query_chat_id(
		pave_event_space())(
			per_chat_id(), create_open, FutureBot, timeout=180),
])

# On first startup, inform all registered users of update
mydb = SQLight(config.database_name)
player = mydb.get_player()
for p in player:
	p_id = p[1]
	print (u'Send message to: ' + unicode(p[2]) + u' ID: ' + unicode(p[1]))
	try:
		bot.sendMessage(p_id, 'UPDATED VERSION AVAILABLE')
	except Exception as e:
		print (u'Unavailable group or user')
mydb.close()

# Start message loop
bot.message_loop(run_forever='Listening ...')
