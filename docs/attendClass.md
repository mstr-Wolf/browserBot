# AttendClass
## Basic Usage
```python
import sys

from browserBot.attendClass import GoogleClass, ZoomClass

if __name__ == "__main__" and len(sys.argv) == 6:
    sys.argv[1].lower()
    if sys.argv[1] == "meet" or sys.argv[1] == "google":
        try:
            benThe_Clock = GoogleClass(code=sys.argv[2], class_length=float(sys.argv[3]), hour=int(sys.argv[4]), minute=int(sys.argv[5]))
            benThe_Clock.run()
        except KeyboardInterrupt:
            sys.exit()
    elif sys.argv[1] == "zoom":
        try:
            benThe_Clock = ZoomClass(code=sys.argv[2], class_length=float(sys.argv[3]), hour=int(sys.argv[4]), minute=int(sys.argv[5]))
            benThe_Clock.run()
        except KeyboardInterrupt:
            sys.exit()

elif __name__ == "__main__" and len(sys.argv) != 6:
    print("Execution example:\n\tpython3 main.py [platform] [code] [length] [target hour] [target minute]")
    print("Platforms:\n\tgoogle (meet)\n\tzoom")

```

## Attributes
### self.length
```
- Description: Intended time to close driver
- Type: float
- Note: 'self.set_class_length' returns hour, minute and, if necessary, second, from the float value of 'self.length'
```

### self.meet_url
```
- Description: Intended class url, given a certain code
- Type: string
- Setter: self.set_meeting_code()
```

### self.__loginData
```
- Description: User's login and password
- Type: dictionary
- Setter: self.setLoginData()
- Getter: self.getLoginData()
```

### self.__driver
```
- Description: Class' selenium driver (Firefox as standard)
- Type: WebDriver (class)
- Setter: self.set_driver()
- Getter: self.get_driver()
```

### self.__login_url
```
- Description: Account's login url
- Type: string
- Setter: self.set_login_url()
- Getter: self.get_login_url()
```

## Methods

### Flow
> Note: Method self.run() calls self.set_driver(), self.execute() and self.shutdownConnection().

- For instant execution:
```
self.set_driver()
self.execute()
self.shutdownConnection()
```
