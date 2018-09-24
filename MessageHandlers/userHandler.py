from Database.SQLight import SQLight
from telepot.namedtuple import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import config
from threading import Timer


# Message with buttons
spielmenu_markup2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Start', callback_data='/start')],
        [InlineKeyboardButton(text='Other Button', callback_data='/test')],])

        
spielmenu_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Start', callback_data='/start')],])

# Timer timeout
def time_out(chat_id, bot):
    print ('Time ran out')
    bot.sendMessage(chat_id, u'Time is up!', reply_markup=spielmenu_markup)


# Handle normal user input ------------------------------------------------------------------------------
def handleUser(command, msg, chat_id, bot):		
    commands = command.split()
    commandcount= len(commands)
    user = msg['from']
    firstname = user['first_name']
    request = firstname + ' : ' + command
    # Commands with '/'  --------------------
    if command=='/start':
        mydb = SQLight(config.database_name)
        mydb.insert_player(chat_id, firstname)
        mydb.close()
        bot.sendMessage(chat_id, config.welcometext.format(firstname), reply_markup=spielmenu_markup)
    elif command=='/rules':
        bot.sendMessage(chat_id, config.welcometext.format(firstname), reply_markup=spielmenu_markup)
    elif commands[0]=='/timer' and commandcount==2:
        timer = Timer(int(commands[1]), lambda: time_out(chat_id, bot))
        timer.start()


    # Messages without '/'  ---------------------------
    if not command.startswith('/'):
        # Handle normal Text Input here
        isGroupchat = chat_id != msg['from']['id']
        if not isGroupchat:
            bot.sendMessage(user['id'], u'I\'m not that smart yet', reply_markup=spielmenu_markup)
