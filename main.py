from meetup import GoogleMeet

hal = GoogleMeet()

hal.login_data = {"user": "lohan.uchoa@edu.unirio.br", "passwd": "UNIRI0x@$82$86"}
hal.driver = "firefox"
hal.doLogin()

hal.new_class()
hal.set_meeting_url(hal.code)

hal.enter_class()
