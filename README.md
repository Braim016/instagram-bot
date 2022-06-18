# Instagram Bot 
This repository contains my files of python codes for an instagram bot that can like posts and follow people.

## Installations
For this repository, you'll need 
- To have python installed
- To install various modules using "pip install module_name"

## Modules Used
Here are the modules used in this repo:
- os
- random
- time
- selenium.common.exceptions
- selenium
- selenium.webdriver.common.by
- constants (in the repo)
- logger_file (in the repo)
- sys

## Known Bugs
Here are the bugs the repo currently has:
- Not being able to like posts and follow people on the same page due to instagram using the same CSS Selectors for the like and follow buttons respectively. The page has to be refreshed
- Whenever instagram modifies its CSS Selectors, changes will need to be made to the codes

## Running the Code
Here are the steps you need to take to run this program:
- Download the code as a zip file from the repo menu
- Unzip the file
- Install the modules listed in this README file (with any method you're okay with)
- Open the command line then chamge the directory to the unzipped file's directory
- On your command line, input "Python run.py" then follow the prompt <br>
<strong>NOTE:</strong> You don't need to run the files from your command line, you can use any IDE you're confortable with. Just make sure you run the "run.py" file as that is the file that integrates all the files into a single executable file.

## Future Releases
In the future releases, the following functions will be added:
- Comment function
- Functionalities from instapy
- Function to screenshot a particular post
- Try/except statements to the login func incase it's already logged in

## Contributing
To make a contribution:
- Fork the repo
- Make Changes
- Send your pull request for review

## Show Love 💓
Show Love by giving the Repo a star...😇
