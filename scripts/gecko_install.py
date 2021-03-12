import os

os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux32.tar.gz -O $HOME/geckodriver-v0.28.0-linux32.tar.gz --show-progress")
os.system("cd $HOME && tar xvfz geckodriver-v0.28.0-linux32.tar.gz && rm geckodriver-v0.28.0-linux32.tar.gz")
