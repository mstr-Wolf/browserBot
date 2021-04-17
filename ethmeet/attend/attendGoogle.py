from time import sleep
import selenium.common.exceptions

from .attend import Attend

class AttendGoogle(Attend):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def goto_meet(self):
        try: self.driver.get(self.meet_url)
        except selenium.common.exceptions.InvalidArgumentException:
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
            return False
        except selenium.common.exceptions.InvalidSessionIdException:
            print("ERROR ****** INVALID SESSION! ******")
            return False
        except AttributeError:
            print("ERROR ****** WEB DRIVER NOT FOUND! ******")
            return False

        for _ in range(25):
            try:
                button = self.driver.find_elements_by_class_name("uArJ5e UQuaGc Y5sE8d uyXBBb xKiqt M9Bg4d".replace(" ", "."))
                button[0].click()
                break
            except IndexError:
                sleep(1)
                continue
        return True

    def set_meeting_url(self, code):
        try:
            code_len = len(code)
        except TypeError:
            print("ERROR ****** {0} not accepted! ******".format(type(code)))
            return False
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
                        return False
                    else:
                        mCode = code
            else:
                print("ERROR ****** Meeting code not accepted! Please check again ******")
                return False

            self.meet_url="https://meet.google.com/%s" % mCode
        return True
