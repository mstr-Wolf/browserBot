from time import sleep
import selenium.common.exceptions

from .attend import AttendMeet

class GoogleMeet(AttendMeet):
    def __init__(self, **kwargs):
        """
        Parameters:\n
            kwargs['code'] (string): Meeting code\n
        """
        super().__init__(**kwargs)
        self.login_url = "google"

    def goto_meet(self):
        try: self.driver.get(self.meet_url)
        except selenium.common.exceptions.InvalidArgumentException:
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
        except selenium.common.exceptions.InvalidSessionIdException:
            return

        for _ in range(25):
            try:
                self.driver.find_element_by_class_name("uArJ5e UQuaGc Y5sE8d uyXBBb xKiqt M9Bg4d".replace(" ", ".")).click()
                break
            except selenium.common.exceptions.NoSuchElementException:
                sleep(1)
                continue

        return

    def doLogin(self):
        self.driver.get(self.login_url)

        #USER
        try:
            self.driver.find_element_by_id("identifierId").send_keys(self.login_data["user"])
            self.driver.find_element_by_id("identifierNext").click()
            try:
                if self.driver.find_element_by_class_name("o6cuMc"):
                    print("ERROR ****** Login failed. Check user and try again! ******")
                    return
            except selenium.common.exceptions.NoSuchElementException: pass
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
            print("ERROR ****** Login failed. Check your connection and try again! ******")
            return
            
        #PASSWORD
        for _ in range(15):
            try:
                self.driver.find_element_by_name("password").send_keys(self.login_data["passwd"])
                break
            except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException):
                sleep(1)
        try:
            self.driver.find_element_by_id("passwordNext").click()
            try:
                if self.driver.find_element_by_class_name("EjBTad"):
                    print("ERROR ****** Login failed. Check your password and try again! ******")
                    return
            except selenium.common.exceptions.NoSuchElementException: pass
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
                print("ERROR ****** Login failed. Check your connection and try again! ******")
                return

    def set_meeting_url(self, code):
        code_len = len(code)
        mCode = ""

        if "https://meet.google.com/" in code:
            self.meet_url = code
        elif "meet.google.com/" in code:
            self.meet_url= "{0}{1}".format("https://", code)
        else:
            if type(code) != type(0) and ((code_len == 12 and code[3] == "-" and code[8] == "-") or code_len == 10):
                for crc in code:
                    if type(crc) == type(0):
                        print("ERROR ****** Meeting code must not contain numbers! ******")
                    else:
                        mCode = code
            else: print("ERROR ****** Meeting code not accepted! Please check again ******")

            self.meet_url="https://meet.google.com/%s" % mCode
        return
