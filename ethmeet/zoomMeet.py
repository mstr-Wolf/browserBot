import selenium.common.exceptions

from .googleMeet import GoogleMeet

class ZoomMeet(GoogleMeet):
    def __init__(self, **kwargs):
        """
        Parameters:\n
            kwargs['code'] (string): Meeting code\n
        """
        super().__init__(**kwargs)
        self.login_url = "zoom"

    def enter_meet(self):
        try:
            self.driver.get(self.meet_url)
            self.driver.find_elements_by_tag_name("a")[4].click()
        except (selenium.common.exceptions.InvalidArgumentException, selenium.common.exceptions.NoSuchElementException):
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
            return
        except selenium.common.exceptions.InvalidSessionIdException:
            return
        self.driver.find_element_by_id("joinBtn").click()
        return

    def set_meeting_url(self, code):
        if "https://zoom.us/j/" in code:
            self.meet_url = code
        else: self.meet_url="https://zoom.us/j/%s" % code
