import sys, os
sys.path.append(os.path.abspath(".") + "/..")

from attendClass import AttendClass

try:
    class_length = float(sys.argv[2])
    hour = int(sys.argv[3].split(":")[0])
    minute = int(sys.argv[3].split(":")[1])
except ValueError:
    print("Length & target time must be integers!")
    sys.exit()

ben = AttendClass(sys.argv[1], class_length = class_length, hour=hour, minute=minute)
ben.run()
