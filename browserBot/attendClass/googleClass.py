from time import sleep
import selenium.common.exceptions

from .attendClass import AttendClass

class GoogleClass(AttendClass):
    def __init__(self, **kwargs):
        """
        Parameters:\n
            'code' (string): Meeting code\n
            'class_length' (float): Class lenght (in minutes)\n
            'hour' (int): Class' start hour\n
            'minute' (int): Class' start minute\n
        """
        super().__init__(**kwargs)
        self.login_url = "https://accounts.google.com/Login?hl=pt-BR"

    def execute(self, **kwargs):
        self.doLogin()

        try: self.driver.get(self.meet_url)
        except selenium.common.exceptions.InvalidArgumentException:
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
            self.close_drive()
        except selenium.common.exceptions.InvalidSessionIdException:
            return
        return

    def doLogin(self):
        start_time = self.get_time()
        self.driver.get(self.login_url)

        #USER
        try:
            self.driver.find_element_by_id("identifierId").send_keys(self.loginData["user"])
            self.driver.find_element_by_id("identifierNext").click()
            try:
                if self.driver.find_element_by_class_name("o6cuMc"):
                    print("ERROR ****** Login failed. Check user and try again! ******")
                    self.close_drive()
                    return
            except selenium.common.exceptions.NoSuchElementException: pass
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
            print("ERROR ****** Login failed. Check your connection and try again! ******")
            self.close_drive()
            return
            
        #PASSWORD
        for _ in range(15):
            try:
                self.driver.find_element_by_name("password").send_keys(self.loginData["passwd"])
                break
            except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException):
                sleep(1)
        try:
            self.driver.find_element_by_id("passwordNext").click()
            try:
                if self.driver.find_element_by_class_name("EjBTad"):
                    print("ERROR ****** Login failed. Check your password and try again! ******")
                    self.close_drive()
                    return
            except selenium.common.exceptions.NoSuchElementException: pass
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
                print("ERROR ****** Login failed. Check your connection and try again! ******")
                self.close_drive()
                return
        print("Login time: ", self.get_time() - start_time)

    def set_meeting_code(self, **kwargs):
        try:
            kwargs["meeting_code"] + "STRING_TEST"
        except TypeError:
            print("ERROR ****** Meeting code must be string! ******")
            self.meet_url =  ""
            return

        code_len = len(kwargs["meeting_code"])
        if code_len != 12 and code_len != 10:
            print("ERROR ****** Meeting code not accepted! Please check again ******")
            self.meet_url =  ""
        elif (code_len == 12 and kwargs["meeting_code"][3] == "-" and kwargs["meeting_code"][8] == "-") or code_len == 10:
            for crc in kwargs["meeting_code"]:
                try:
                    int(crc)
                    print("ERROR ****** Meeting code must not contain numbers! ******")
                    self.meet_url =  ""
                    return
                except ValueError: continue
            self.meet_url="https://meet.google.com/%s" % kwargs["meeting_code"]