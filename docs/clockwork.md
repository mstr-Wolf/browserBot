# clockwork Class
```python
class Clockwork():
    def __init__(self, **kwargs):
        self.__time_now = Delorean().now()
        try:
            self.__target = self.__time_now.replace(hour = kwargs["hour"], minute = kwargs["minute"], second = 0)
        except KeyError:
            print("Time not provided!")
            sys.exit(1)
```

#### Parameters
- kwargs["hour"] *(int)*: Hour
- kwargs["minute"] *(int)*: Minute

#### Attributes
- self.__time_now *(delorean.Delorean)*: Datetime informations returned from Delorean
- self.__target *(delorean.Delorean)*: Target time

## run Method
```python
def run(self):
    print(__name__, "started!")
    print("Process scheduled to", self.__target.format_datetime(), "\n")
    while True:
        print(self.get_time().format_datetime(), end="\r")
        if self.__time_now == self.__target or self.__time_now > self.__target:
            print("Time reached\nStarting process...")
            try:
                    self.execute()
            except:
                print("ERROR TRYING TO GET URL")
            finally:
                sys.exit(0)
        sleep(1)
```
##### Description
Countdown till target time be reached and, then, executes method <self.execute>

##### Parameters
- None

##### Returns
- None

## execute Method
```python
def execute(self, **kwargs):
    raise NotImplementedError
```
> Method must be implemented for each child class

##### Parameters
- Takes dictionary as parameter

##### Returns
- None

## get_time Method
```python
def get_time(self):
        self.__time_now = self.__time_now.now()
        self.__time_now.truncate("second")
        return self.__time_now
```
##### Description
Returns Clockwork.__time_now (mainly) for child classes

##### Returns
- Delorean


## get_target Method
```python
def get_target(self):
    return self.__target
```
##### Description
Returns Clockwork.__target (mainly) for child classes

##### Returns
- Delorean


## reset_target Method
```python
def reset_target(self, **kwargs):
    self.__target = self.__target.replace(hour = kwargs["hour"], minute = kwargs["minute"], second = 0)
```
##### Description
Updates Clockwork.__target with any given hour and minute. Seconds are 0 as standard.

##### Returns
- None

## delay_target Method
```python
def delay_target(self, **kwargs):
    self.__target = self.get_time() + timedelta(hours=kwargs["hour"], minutes=kwargs["minute"])
```
##### Description
Delays Clockwork.__target (only forward) with a given hour and minute. Seconds are the same as to Clockwork.__time_now.

##### Returns
- None
