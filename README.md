# ethmeet
Video-chat API. Compatible with most famous platforms.

## Installation
Pip:
```shell script
pip3 install ethmeet
```

Install Geckodriver:
```shell script
python3 /usr/local/bin/gecko_install.py
```

## Docs
- [API Reference](https://github.com/elleaech/ethmeet/blob/master/docs/ethmeet.md)

### Basic Usage
``` python
from ethmeet import (Driver, AttendGoogle, CreateGoogle, LoginGoogle)

# SET COMMON DRIVER
driver = Driver()


# INSTANCE OBJECTSs
adm_login = LoginGoogle(driver = driver())

create = CreateGoogle(driver = driver())

login = LoginGoogle(driver = driver())

attend = AttendGoogle(driver = driver())


# SET LOGIN DATA
adm_login.login_data = {"some.email@service.com", "SomePa$$word123"}

# IF LOGIN IS SUCCESSFUL, CREATE NEW MEET CODE
if adm_login.doLogin():
        create.new_meet()

# GET LOGIN INPUT
login.login_data = {}

# IF LOGIN IS SUCCESSFUL AND MEET CODE WAS CREATED, GO TO MEETING
if login.doLogin() and create.code != None:
        attend.set_meeting_url(create.code)
        attend.goto_meet()


# CLOSE DRIVER
driver.close()
```

## Contributing & Issue Tracker
Branch & [Pull Request](https://github.com/elleaech/ethmeet/pulls)
- [Issues](https://github.com/elleaech/ethmeet/issues)

### Get source
```shell script
git clone git@github.com:elleaech/ethmeet.git && cd ethmeet

python3 -m virtualenv . && pip3 install -r requirements.txt
```

## License
[Apache License 2.0](https://github.com/elleaech/ethmeet/blob/master/LICENSE)
