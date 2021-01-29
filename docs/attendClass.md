# AttendClass
## Basic Usage
```python
import sys

from time import sleep
TIME = 10 #class length in seconds

from browserBot.attendClass import GoogleClass, ZoomClass

hall = GoogleClass(code = "aaabbbbccc")
#hall = ZoomClass("some zoom meeting code or url here")

hall.set_login_data(user=<user>, passwd=<password>)
# No parameters for CLI input

hall.driver = "firefox"

hall.doLogin()

hall.enter_class()

for _ in range(TIME): sleep(1)

hall.driver.close()
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
