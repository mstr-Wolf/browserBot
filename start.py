import sys
from src import (clockwork, read_file_content, last_date_recovery)

if __name__=="__main__":
    try:
        play = read_file_content()
    except (ValueError, IndexError):
        print("FILE CORRUPTED!")
        sys.exit(0)
    if play == False: sys.exit(0)

    if len(sys.argv) == 1:
        last_date_recovery()
        sys.exit(0)
    if sys.argv[1] == "--help":
        print("[PYTHON COMPILER] start.py [HOUR:MINUTE:SECOND] [URL]")
        last_date_recovery()
    else:
        try:
            target_time = sys.argv[1].split(":")
            ben = clockwork(URL=sys.argv[2], hour=int(target_time[0]),
                        minute=int(target_time[1]),
                        second=int(target_time[2]),)
            ben.run()
        except KeyboardInterrupt:
            last_date_recovery()
            sys.exit(1)
        except IndexError:
            print("INCOMPLETE DATA")
            last_date_recovery()
            sys.exit(0)
        except ValueError:
            print("WRONG DATA")
            last_date_recovery()
            sys.exit(0)