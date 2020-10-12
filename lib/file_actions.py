from datetime import datetime

DATETIME_NOW = datetime.now()

def read_file_content():
    with open("lib/boot", "r+") as file_:
        line = file_.readlines()[0]
        date = line.split()
        if int(date[1]) < DATETIME_NOW.day or int(date[0]) < DATETIME_NOW.month:
            file_.seek(0)
            file_.write("{} {}".format(str(DATETIME_NOW.month), str(DATETIME_NOW.day)))
            return True
        else: return False

def last_date_recovery():
    with open("lib/boot", "w") as file_:
        file_.write("{} {}".format(str(DATETIME_NOW.month), str(DATETIME_NOW.day-1)))