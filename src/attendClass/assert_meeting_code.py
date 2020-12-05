import sys

def assert_meeting_code(meeting_code, min_len, max_len):
    try: meeting_code + "STRING_TEST"
    except TypeError:
        print("Meeting code must be string!")
        sys.exit(0)

    code_len = len(meeting_code)
    if code_len != max_len and code_len != min_len:
        print("Meeting code not accepted! Please check again")
        sys.exit(0)
    elif (code_len == max_len and meeting_code[3] == "-" and meeting_code[8] == "-") or code_len == min_len:
        for crc in meeting_code:
            try:
                int(crc)
                print("Numbers are not accepted!")
                sys.exit(0)
            except ValueError: continue
        return "https://meet.google.com/%s" % meeting_code