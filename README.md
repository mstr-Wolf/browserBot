# ethmeet
Automate online meetings with ethmeet library.

## Installation
Pip:
```shell script
pip3 install ethmeet
```
> NOTE: ethmeet module uses Firefox as its standard browser

## Docs
- [AttendMeet Basic Usage](https://github.com/sourcerer0/ethmeet/blob/master/docs/attendMeet.md)
- [CreateMeet Basic Usage](https://github.com/sourcerer0/ethmeet/blob/master/docs/createMeet.md)
### Basic Usage
```python
import sys

from time import sleep
TIME = 10 #class length in seconds

from ethmeet import GoogleMeet, ZoomMeet

hall = GoogleMeet(code = "aaabbbbccc")
#hall = ZoomMeet("some zoom meeting code or url here")

hall.login_data = {"user": "<your username>",
                "passwd": "<your password>"}
# hall.login_data = {} for CLI input

hall.driver = "firefox"

hall.doLogin()

hall.goto_meet()

for _ in range(TIME): sleep(1)

hall.driver.close()
```

## Contributing & Issue Tracker
Branch & [Pull Request](https://github.com/sourcerer0/ethmeet/pulls)
- [Issues](https://github.com/sourcerer0/ethmeet/issues)

### Get source
```shell script
git clone git@github.com:sourcerer0/ethmeet.git && cd ethmeet

python3 -m virtualenv . && pip3 install -r requirements.txt
```

## License
[Apache License 2.0](https://github.com/sourcerer0/ethmeet/blob/master/LICENSE)
