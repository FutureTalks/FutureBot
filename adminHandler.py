from SQLight import SQLight
from telepot.namedtuple import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import config


def handleAdmin(command, msg, chat_id, bot):
    commands = command.split()
    # Commands with '/'  ----------------------
    if commands[0]=='/broadcast':
        # Send a message to all users
        message = command.replace(commands[0], '')
        mydb = SQLight(config.database_name)
        player = mydb.get_player()
        for p in player:
            p_id = p[1]
            print (u'Send message to: ' + unicode(p[2]) + u' ID: ' + unicode(p[1]))
            bot.sendMessage(p_id, message)
        mydb.close()
    elif commands[0]=='/test':
        # Send buttons like this
        rating_markup = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Test', callback_data='/test')],
                [InlineKeyboardButton(text='Test', callback_data='/test')],])
        bot.sendMessage(chat_id, 'Test', reply_markup=rating_markup)