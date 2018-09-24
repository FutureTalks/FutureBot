# FutureBot
## What is it?

FutureBot (http//t.me/futureTalksBot) is a collaborative Telegram Bot Project with continuous deployment to a Raspberry Pi (Very nice tutorial on how to achieve this here: http://thesociablegeek.com/node/github-continuous-deployment-to-a-raspberry-pi/).

The current setup is a very basic bot with not many features, what happens with it is up to you. You are invited to improve the bot in any way you see fit. Better conventions, general feedback and tips for improved collaboration are always welcome.

On a merge into the main branch of this repository, the Raspberry running the FutureBot (http//t.me/futureTalksBot) will automatically pull and run the latest version. After pulling, it will first run 'init_database.py' and then execute 'bot.py'. It will also automatically inform all previous users that an update is available. And that's all it takes. 

To get your own Telegram Bot to develop new features and start extending FutureBot, follow the instructions below.


## Instructions

* **Fork & Clone this project**


* **Install Anaconda 5.x (Python 2.7)** - (Should we upgrade to Python 3?)

    Anaconda is an easy solution to set up Python on different systems

	https://www.anaconda.com/download/

	Don't forget to set Path variables after install (Probably something like 'C:/Users/x/AnacondaX' and 'C:/Users/x/AnacondaX/Scripts')
	

* **Install Visual Studio Code (Recommended, you can use any other IDE of your choice)**
    In Visual Studio Code install Python extension. You should now be able to choose Anaconda as your Python environment to run the code


* **Create your personal bot token using the Telegram Botfather (http://t.me/botfather). This will be the token for your personal development-bot**


* **Create a file "customConfig.py" in the root folder of this project with the lines:**

    token = 'XXX:XXXXX' # Paste your previously created bot token instead of XXX:XXXXX

    admins = [00000,11111,33333] # Find out your id and add it to the list


* **In your terminal run:**

    'python init_database.py' (Once, to initialize your database)

    'python bot.py' (To start your bot, you may have to install packages (telepot, boto3,...) using pip)
 

* **Use your own bot to develop and test extensions. Pull requests / Merges into the main branch of the repository will be running in the main bot: (http//t.me/futureTalksBot).**
    The connected Raspberry first runs 'init_database.py' (To initialize new db if necessary) after a pull and then executes 'bot.py'.


* **Have fun**


## References
Telepot: https://telepot.readthedocs.io/en/latest/index.html#an-easier-way-to-receive-messages
Telegram Bot API: https://core.telegram.org/bots/api


## House Rules
* Do not intentionally break the Bot / Raspberry.
* Only do pull requests into the master branch of the FutureBot repository, never do a direct commit.
* Never commit any personal API-Keys into a public repository! Keep them in your customConfig (.gitignored) or anywhere else and explain somewhere how to get a key for the used API.
* Stay Awesome