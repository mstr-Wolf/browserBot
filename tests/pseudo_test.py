from ethmeet import GoogleMeet
from ethmeet.create import CreateGoogle
from ethmeet.login import GoogleLogin
from ethmeet.driver import Driver

from time import sleep


# SET WEB DRIVER
web_driver = Driver()
web_driver.driver = "firefox"


# LOGIN
myAccount = GoogleLogin(driver = web_driver)

myAccount.login_url = "google"
# myAccount.login_url = "zoom"

myAccount.login_data = {}
myAccount.doLogin()


# CREATE NEW MEET
adm = CreateGoogle(driver = web_driver)
adm.new_meet()


# GO TO MEET
meet = GoogleMeet(driver = web_driver, code = adm.code)
meet.goto_meet()


# CLOSE CONNECTION
for _ in range(5): sleep(1)
web_driver.driver.close()
