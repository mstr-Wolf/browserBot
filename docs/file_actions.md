# read_file_content Function
```python
def read_file_content():
    with open("lib/boot", "r+") as file_:
        date = file_.readlines()[0].split()
        if int(date[1]) < DATETIME_NOW.day or int(date[0]) < DATETIME_NOW.month:
            file_.seek(0)
            file_.write("{} {}".format(str(DATETIME_NOW.month), str(DATETIME_NOW.day)))
            return True
        else: return False
```
#### Description
1. Reads the first line of 'lib/boot' file
1. Verify if last time activate was today
1. Writes new date

#### Parameters
- None

#### Variables
- date *(string)*: Take date stored in 'lib/boot' file

#### Returns
- boolean type *(True/False)*

# last_date_recovery Function
```python
def last_date_recovery():
    with open("lib/boot", "w") as file_:
        file_.write("{} {}".format(str(DATETIME_NOW.month), str(DATETIME_NOW.day-1)))
```

#### Description
Rewrites 'lib/boot' date info by decreasing, of the current day, one

#### Parameters
- None

#### Variables
- None

#### Returns
- None
