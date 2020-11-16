import sys
from src import (clockwork, read_file_content, last_date_recovery)

if __name__=="__main__":
    if sys.argv[1] == "--help":
        print("[PYTHON COMPILER] start.py [HOUR:MINUTE:SECOND] [URL]")
        sys.exit(0)
    else:
        try:
            target_time = sys.argv[1].split(":")
            ben = clockwork(URL=sys.argv[2], hour=int(target_time[0]),
                        minute=int(target_time[1]),
                        second=int(target_time[2]),)
            ben.run()
        except KeyboardInterrupt:
            pass
        except IndexError:
            print("INCOMPLETE DATA")
        except ValueError:
            print("WRONG DATA")
        finally:
            sys.exit(0)