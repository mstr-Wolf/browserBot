from ethmeet import GoogleMeet
from ethmeet.create import CreateGoogle
from ethmeet.login import GoogleLogin
from ethmeet.driver import Driver

from time import sleep


login_data = {}


# SET WEB DRIVER
adm_driver = Driver(auto_start = True)
web_driver = Driver(auto_start = True)


# LOGIN 1
adm_login = GoogleLogin(driver = adm_driver)
adm_create = CreateGoogle(driver = adm_driver)
adm_meet = GoogleMeet(driver = adm_driver)

adm_login.login_url = "google"
# myAccount.login_url = "zoom"
adm_login.login_data = login_data

if adm_login.doLogin(): adm_create.new_meet()

"""
if adm_login.doLogin() and adm_create.new_meet():
        adm_meet.set_meeting_url(adm_create.code)
        adm_meet.goto_meet()
else:
        print("Login failed or new meet not created! Skipping...\n")
"""




# LOGIN 2
myAccount = GoogleLogin(driver = web_driver)
meet = GoogleMeet(driver = web_driver)

myAccount.login_url = "google"
# myAccount.login_url = "zoom"
myAccount.login_data = login_data

if myAccount.doLogin() and adm_create.code != None:
        meet.set_meeting_url(adm_create.code)
        meet.goto_meet()
        adm_driver.driver.close()
else:
        print("Login failed or code unset! Skipping...\n")



# CLOSE CONNECTION
for _ in range(30): sleep(1)
web_driver.driver.close()
