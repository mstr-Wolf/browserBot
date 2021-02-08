# AttendMeet
## Basic Usage
```python
import sys

from time import sleep
TIME = 10 #class length in seconds

from meetup import GoogleMeet, ZoomMeet

hall = GoogleMeet(code = "aaabbbbccc")
#hall = ZoomMeet("some zoom meeting code or url here")

hall.login_data = {"user": "<your username>",
                "passwd": "<your password>"}
# hall.login_data = {} for CLI input

hall.driver = "firefox"

hall.doLogin()

hall.enter_class()

for _ in range(TIME): sleep(1)

hall.driver.close()
```

## Attributes
### self.meet_url
- Description: Intended class url, given a certain code
- Type: string

Setter:
```python
#defined at __init__(), by kwargs['code'] parameter (don't need to worry)
self.set_meeting_url("code or url")
```

### self.login_url
- Description: Account's login url
- Type: string

Setter:
```python
#defined by child class at __init__() (don't need to worry)
self.login_url = "<platform>"

"""
Platforms:
    - google / meet
    - zoom
"""
```

### self.login_data
- Description: User's login and password
- Type: dictionary

Setter:
```python
self.login_data = {} #for CLI input

self.login_data = {"user": "",
                "passwd": ""}
```

### self.driver
- Description: Class' selenium driver (Firefox as standard)
- Type: WebDriver (class)

Setter:
```python
self.driver = "<platform>"

"""
Platforms:
    - firefox
"""
```
