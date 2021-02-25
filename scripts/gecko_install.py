import subprocess

download = ["wget", "https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux32.tar.gz", "-O", "$HOME/geckodriver-v0.28.0-linux32.tar.gz",  "--show-progress"]
extract = ["cd", "$HOME", "&&", "tar", "xvfz", "geckodriver-v0.28.0-linux32.tar.gz"]

if subprocess.call(download) == 0:
    subprocess.call(extract)
