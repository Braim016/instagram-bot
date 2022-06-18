# Importing the functionalities file
from Instagram_Bot.functionalities import InstaFunction
from Instagram_Bot.constants import task, username, password

# Creating a context manager
with InstaFunction() as bot:
    bot.land_home_page()
    bot.log_in(username, password)
    bot.authenticate()
    if task.lower() == 'like':
        bot.liking_posts()
    elif task.lower() == 'follow':
        bot.following_people()
