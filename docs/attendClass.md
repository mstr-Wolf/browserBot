# AttendClass
## Basic Usage
```python
from browserBot.attendClass import GoogleClass, ZoomClass

hall = GoogleClass("aaabbbbccc")
#hall = ZoomClass("some zoom meeting code or url here")

hall.set_login_data(user=<user>, passwd=<password>)
# No parameters for CLI input

hall.driver = "firefox"

hall.doLogin()

hall.enter_class()
```

## Attributes
### Defined on __init__()
#### self.meet_url
```
- Description: Intended class url, given a certain code
- Type: string
```

#### self.login_url
```
- Description: Account's login url
- Type: string
```

### self.login_data
```
- Description: User's login and password
- Type: dictionary
```

### self.driver
```
- Description: Class' selenium driver (Firefox as standard)
- Type: WebDriver (class)
```

## Advanced Usage
```python
import sys

from browserBot.attendClass import GoogleClass, ZoomClass

if __name__ == "__main__" and len(sys.argv) == 2:
    sys.argv[1].lower()
    if sys.argv[1] == "meet" or sys.argv[1] == "google":
        try:
            benThe_Clock = GoogleClass(code=sys.argv[2])
        except KeyboardInterrupt:
            sys.exit()
    elif sys.argv[1] == "zoom":
        try:
            benThe_Clock = ZoomClass(code=sys.argv[2])
        except KeyboardInterrupt:
            sys.exit()

elif __name__ == "__main__" and len(sys.argv) != 2:
    print("Execution example:\n\tpython3 main.py [platform] [code] [length] [target hour] [target minute]")
    print("Platforms:\n\tgoogle (meet)\n\tzoom")

```
