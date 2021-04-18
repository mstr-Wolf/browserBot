from ethmeet import AttendGoogle
from ethmeet import CreateGoogle
from ethmeet import LoginGoogle
from ethmeet import Driver

from time import sleep


login_data = {}


# SET WEB DRIVER
adm_driver = Driver(auto_start = True)
# adm_driver.__start()




# LOGIN 1
adm_login = LoginGoogle(driver = adm_driver.driver)
adm_create = CreateGoogle(driver = adm_driver.driver)


adm_login.login_data = login_data

if adm_login.doLogin():
        adm_create.new_meet()




# LOGIN 2
myAccount = LoginGoogle(driver = adm_driver.driver)

meet = AttendGoogle(driver = adm_driver.driver)

myAccount.login_data = login_data

if myAccount.doLogin() and adm_create.code != None:
        meet.set_meeting_url(adm_create.code)
        meet.goto_meet()
else:
        print("Login failed or code unset! Skipping...\n")



# CLOSE CONNECTION
print("Closing process initiated!")
for _ in range(15):
        sleep(1)
adm_driver.driver.close()
