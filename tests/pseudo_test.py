from ethmeet import GoogleMeet
from ethmeet.create import CreateGoogle
from ethmeet.login import GoogleLogin
from ethmeet.driver import Driver


# SET WEB DRIVER
web_driver = Driver()
web_driver.driver = "firefox"


# LOGIN
myAccount = GoogleLogin(web_driver)

myAccount.login_url = "google"
# myAccount.login_url = "zoom"

myAccount.login_data = {}
myAccount.doLogin()


# CREATE NEW MEET
adm = CreateGoogle(web_driver)
adm.new_meet()


# GO TO MEET
meet = GoogleMeet(web_driver, code = adm.code)
meet.goto_meet()
