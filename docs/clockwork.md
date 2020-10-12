# clockwork Class
```python
class clockwork():
    def __init__(self, timezone, givenURL, **kwargs):
        super().__init__()
        self.__time_now = Delorean(timezone=timezone)
        try:
            self.__target = Delorean(datetime = DATETIME_NOW,timezone=timezone).replace(hour = kwargs["hour"],
                                                                                    minute = kwargs["minute"],
                                                                                    second = kwargs["second"])
        except:
            print("Time not provided!")
            sys.exit(1)
        self.__URL = givenURL
```
#### Description
Initiate the class


#### Parameters
- timezone *(string)*: The timezone from your current location
- givenURL *(string)*: Browser URL
- kwargs["hour"] *(int)*: Hour
- kwargs["minute"] *(int)*: Minute
- kwargs["second"] *(int)*: Second

#### Attributes
- self.__time_now *(delorean.Delorean)*: Datetime informations returned from Delorean
- self.__target *(delorean.Delorean)*: Target time
- self.__URL *(string)*: Requested URL

#### Returns
- None

## run Function
```python
def run(self):
        while True:
            self.get_time()
            print(self.__time_now.format_datetime(), "\n")
            if self.__time_now == self.__target or self.__time_now > self.__target: 
                print("Time reached\nStarting service...")
                try:
                    open_url(self.URL)
                except:
                    print("ERROR TRYING TO OPEN URL")
                    raise
                finally:
                    sys.exit(0)
            sleep(1)
```
##### Description
Works as a cronometer, waits till target time be reached

##### Parameters
- Instanced Object

##### Returns
- None
