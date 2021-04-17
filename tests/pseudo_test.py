from ethmeet.attend import AttendGoogle
from ethmeet.create import CreateGoogle
from ethmeet.login import LoginGoogle
from ethmeet.driver import Driver

from time import sleep


login_data = {}


# SET WEB DRIVER
adm_driver = Driver(auto_start = True)
# adm_driver.__start()




# LOGIN 1
adm_login = LoginGoogle(driver = adm_driver.driver)
adm_create = CreateGoogle(driver = adm_driver.driver)


adm_login.login_data = login_data

if adm_login.doLogin(): adm_create.new_meet()

"""
adm_meet = AttendGoogle()
adm_meet.driver = adm_driver

if adm_login.doLogin() and adm_create.new_meet():
        adm_meet.set_meeting_url(adm_create.code)
        adm_meet.goto_meet()
else:
        print("Login failed or new meet not created! Skipping...\n")
"""




# LOGIN 2
myAccount = LoginGoogle(driver = adm_driver.driver)

meet = AttendGoogle(driver = adm_driver.driver)

myAccount.login_data = login_data

if myAccount.doLogin() and adm_create.code != None:
        meet.set_meeting_url(adm_create.code)
        meet.goto_meet()
        adm_driver.driver.close()
else:
        print("Login failed or code unset! Skipping...\n")



# CLOSE CONNECTION
print("Closing process initiated!")
for _ in range(15): sleep(1)
myAccount.driver.close()
