# importing os for the path variable thingy
import os
# To randomize things so that my server won't be blocked
import random
# To send requests at regular intervals
import time
# normal importing webdriver from the selenium package
# import selenium.common.exceptions
import selenium.common.exceptions
from selenium import webdriver
# All these were imported so that it can use the "By" argument inside the find_element method
from selenium.webdriver.common.by import By
# To bring the constants from the constants file
from instagram_bot import constants as const
# To log information
from logger_file import *


# So, let's start with creating a class
class InstaFunction(webdriver.Chrome):

    # Creating the init function
    def __init__(self, teardown=False, driver_path=r'C:\Selenium py\chromedriver_win32'):
        self.driver_path = driver_path
        self.teardown = teardown
        # Specifying the path from environs
        os.environ['PATH'] += self.driver_path
        # ?
        super(InstaFunction, self).__init__()
        # TO wait 45 sec
        self.implicitly_wait(45)
        # To maximize window
        self.maximize_window()

    # Creating a function for exiting the test run
    def __exit__(self, exc_type, exc_val, exc_tb):
        # To shut down the browser when we're done with everything
        # Now, creating a closing condition
        if self.teardown:
            self.quit()

    # Creating a function to go to the home page
    def land_home_page(self):
        logger.info("Let's get you started")
        self.get(const.instagram_site)

    # To initiate the login procedures
    def log_in(self, email, password):
        # Finding the login ID field
        email_login = self.find_element(By.CSS_SELECTOR, 'input[aria-label="Phone number, username, or email"]')
        # Sending the keys to the login ID field
        email_login.send_keys(email)
        # Finding the password field
        pass_login = self.find_element(By.CSS_SELECTOR, 'input[aria-label="Password"]')
        # Sending the keys to the password field
        pass_login.send_keys(password)
        # Finding the Login button
        enter_button = self.find_element(By.CSS_SELECTOR, 'button[class="sqdOP  L3NKy   y3zKF     "]')
        # Clicking the login button
        enter_button.click()
        try:
            button = self.find_element(By.CSS_SELECTOR, 'p[data-testid="login-error-message"]')
            if button:
                logger.error("Kindly check your login details to make sure they're correct or check your connection "
                             "and try again later.\nExiting...")
                time.sleep(5)
                self.quit()
        except selenium.common.exceptions.NoSuchElementException:
            logger.info("Login Successful")

    # After login, there might be some extra authentications needed
    def authenticate(self):
        try:
            # Checking if instagram is asking us to save login info
            save_info = self.find_element(By.CSS_SELECTOR, 'button[class="sqdOP  L3NKy   y3zKF     "]')
            # Clicking if we find the field
            save_info.click()
        finally:
            # The notification pop up might not show up immediately, so we wait small
            time.sleep(5)

        try:
            # Checking if the notification popup pops up
            notifications = self.find_element(By.CSS_SELECTOR, 'button[class="_a9-- _a9_1"]')
            # Clicking if we find the function
            notifications.click()
        finally:
            pass

    # Now, we need a function for liking random posts
    def liking_posts(self):
        # Creating a starting value
        count_like = 0
        # Creating an iteration over the number of likes we want
        for i in range(const.like_post_amount):
            # Randomizing the sleeping time
            timex = random.randint(20, 30)
            # Finding the like button on the home page
            like_post = self.find_element(By.CSS_SELECTOR, 'span[class="_aamw"]')
            # Clicking the like button
            like_post.click()
            # Increasing the count variable to know the amount of posts we've liked so far
            count_like += 1
            # Printing the amount of posts we've liked so that the user will know the progress of the
            logger.info(f"I've successfully liked {count_like} post(s)")
            # Checking to know if we've reached the number of likes required
            if count_like == const.like_post_amount:
                break
            # Returning the number of posts left to like
            logger.info(f"{const.like_post_amount - count_like} Post(s) to go...")
            # Returning the next waiting time
            logger.info(f"We'll be waiting for {timex} seconds")
            # Delaying the program so that my servers won't be flagged by Instagram
            time.sleep(timex)
            # Returning the current status
            logger.info('Refreshing...')
            # Refreshing the page to get a post to like as the CSS elements don't allow for multiple likes on the
            # same page
            self.refresh()
            # Delaying the program a little incase there is a connectivity issue
            time.sleep(3)
            # Returning the current status of the code
            logger.info('Done Refreshing')
        # Taking the time the program finished
        like_end_time = time.perf_counter()
        # Returning the final report for the program
        logger.info(f"Task Completed in {round((like_end_time - const.start_time), 2)} seconds.")
        logger.info("Thank you for using our service.\nDo have a wonderful day ahead.\nRegards, Salman.")
        # Waiting 10 seconds so that user can see the final result before the window closes
        time.sleep(10)
        # Exiting the window
        self.quit()

    def following_people(self):
        # Finding the "explore" people page
        go_to_follow_page = self.find_element(By.CSS_SELECTOR, 'a[href="/explore/people/"')
        # Clicking on the "explore" people page
        go_to_follow_page.click()
        # Creating a variable to
        count = 0
        # Creating an iteration over the number of people we want to follow
        for i in range(const.follow_amount):
            # Randomizing the sleeping time
            timex = random.randint(20, 30)
            # Sleeping so that the page will load before finding the CSS Selector
            time.sleep(10)
            # Finding and clicking the button to follow the first person on the list
            follow_people = self.find_element(By.CSS_SELECTOR, 'button[class="_acan _acap _acas"]')
            follow_people.click()
            # Incrementing the count by 1
            count += 1
            # Updating the status
            logger.info(f"I've successfully followed {count} account(s)")
            # Checking if the count is equal to the number of persons the user wants to follow
            if count == const.follow_amount:
                break
            # Updating the status of the program
            logger.info(f"{const.follow_amount - count} person(s) to go...")
            logger.info(f"Now, we'll be waiting for {timex} seconds")
            # Sleeping the program so that instagram won't flag the account
            time.sleep(timex)
            # Status update
            logger.info('Refreshing...')
            # Refreshing page
            self.refresh()
            # Letting the program sleep for 5 mins to wait for the refresh to be completed
            time.sleep(5)
            logger.info('Done Refreshing')
        # Getting the end time
        follow_end_time = time.time()
        # Final report
        logger.info(f"Task Completed in {round((follow_end_time - const.start_time), 2)} seconds.")
        logger.info("Thank you for using our service.\nDo have a wonderful day ahead.\nRegards, Salman.")
        self.quit()

    # Creating a function to check if we're logged in
    # def check_logging_status(self):
    #     return
