# Schedule Requests
Open your favorite hosts automatically in your browser

# Installation
```shell script
git clone https://github.com/mstr-Wolf/scheduleRequest.git
```

## Dependancies
#### Package Installer:
```shell script
pip3 install -r requirements.txt
```
#### Pypy Compiler
```shell script
pypy3 -m ensurepip
pypy3 -m pip install -r requirements.txt
```

# Basic Usage
```python
from clockwork import clockwork
import sys

target_time = ["10", "00","00"]
ben = clockwork("America/Sao_Paulo",
            "https://github.com/mstr-Wolf/scheduleRequest.git",
            hour=int(target_time[0]),
            minute=int(target_time[1]),
            second=int(target_time[2]),)
ben.run()
```
**or run the script at command line:**
```shell script
python3 start.py America/Sao_Paulo 10:00:00 https://www.youtube.com/watch?v=ZdJ6FO9HAcc
```
**or even**
```shell script
pypy3 start.py America/Sao_Paulo 10:00:00 https://www.youtube.com/watch?v=ZdJ6FO9HAcc
```

# API Reference
Link: *https://github.com/mstr-Wolf/scheduleRequest/tree/master/docs*

# [Contributing](https://github.com/mstr-Wolf/scheduleRequest/issues)
**Also, feel free to fork it any time!**

# License
[Apache License 2.0](https://github.com/mstr-Wolf/scheduleRequest/blob/master/LICENSE)

# Contact
- Gmail
    - lohan.uchoa@edu.unirio.br
    - lohan.chuan123@gmail.com