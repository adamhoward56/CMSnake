import os
import shutil
import datetime

PROJECT_NAME = "site"

# Completely re-builds the website
def rebuild():
    global PROJECT_NAME
    if os.path.exists(PROJECT_NAME):
        shutil.rmtree(PROJECT_NAME)
    os.mkdir(PROJECT_NAME)

rebuild()