from sys import exit
from clockwork import Clockwork

class AttendClass(Clockwork):
    def __init__(self, code, **kwargs):
        super().__init__(**kwargs)
        self.MEET_URL = self.assert_meeting(code, 10, 12)

    def execute(self, **kwargs):
        pass

    def assert_meeting(self, meeting_code, min_len, max_len):
        try: meeting_code + "STRING_TEST"
        except TypeError:
            print("Meeting code must be string!")
            exit(0)

        code_len = len(meeting_code)
        if code_len != max_len or code_len != min_len:
            print("Meeting code not accepted! Please check again")
            exit(0)
        elif (code_len == max_len and meeting_code[3] == "-" and meeting_code[8] == "-") or code_len == min_len:
            for crc in meeting_code:
                try:
                    int(crc)
                    print("Numbers are not accepted!")
                    exit(0)
                except ValueError: continue
            return "https://meet.google.com/%s" % meeting_code
