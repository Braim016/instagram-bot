import logging
import sys
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s', datefmt='%d/%m/%y %H:%M:%S')

file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Starting the timer
start_time = time.perf_counter()

instagram_site = 'https://www.instagram.com'

# Taking inputs and creating control flow
task = input("Hi. I'm betty, an instagram bot made by Salman. Would you like me to help you follow people or like "
             "posts today?\nKindly input either 'follow' or 'like'\n>>>")
if task.lower() == 'like':
    try:
        like_post_amount = int(input("How many posts do you want me to like for you today?\n>>>"))
    except ValueError:
        logger.error("The necessary input for this field is an integer\nExiting...")
        sys.exit()
elif task.lower() == 'follow':
    try:
        follow_amount = int(input("How many people do you want me to follow for you today?\n>>>"))
    except ValueError:
        logger.error("The necessary input for this field is an integer\nExiting...")
        sys.exit()
else:
    logger.error('I can only help you like posts and follow people for now\nExiting...')
    sys.exit()
username = input("Kindly input your username/email to get started\n>>>")
password = input("Kindly input your password\n>>>")
