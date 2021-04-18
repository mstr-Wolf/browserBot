import selenium.common.exceptions

from .attendGoogle import AttendGoogle

class AttendZoom(AttendGoogle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def goto_meet(self):
        try:
            self.driver.get(self.meet_url)
            self.driver.find_elements_by_tag_name("a")[4].click()
        except (selenium.common.exceptions.InvalidArgumentException, selenium.common.exceptions.NoSuchElementException):
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
            return False
        except selenium.common.exceptions.InvalidSessionIdException:
            print("ERROR ****** INVALID SESSION! ******")
            return False
        except AttributeError:
            print("ERROR ****** WEB DRIVER NOT FOUND! ******")
            return False

        self.driver.find_element_by_id("joinBtn").click()
        return True

    def set_meeting_url(self, code):
        if "https://zoom.us/j/" in code:
            self._Attend__meet_url = code
        else: self._Attend__meet_url="https://zoom.us/j/%s" % code

        return True
