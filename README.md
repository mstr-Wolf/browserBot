# browserBot
Attending online classes? Scraping website data? Building bots? 

'browserBot' is an easy way to automate web through your browser. 

Let your imagination drive you...

## Installation
Get source code
```shell script
git clone https://github.com/sourcerer2/browserBot.git && cd browserBot

# In case you're having problems with QT_DEVICE_PIXEL_RATIO
./QT_DEVICE.sh
```

### Dependancies
#### Package Installer
```shell script
pip3 install -r requirements.txt
```

#### Browser
*NOTE: attendClass module uses Firefox as its standard browser*

##### Geckodriver Install (Linux)
```shell script
wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux32.tar.gz -O $HOME/geckodriver-v0.28.0-linux32.tar.gz --show-progress

tar xvfz geckodriver-v0.28.0-linux32.tar.gz .
```

## [API Reference](https://github.com/mstr-Wolf/browserBot/tree/master/docs)

## Contributing & Issue Tracker
- [Issues](https://github.com/mstr-Wolf/browserBot/issues)
- Branches: master(stable), where approved features, patches and updates from v.0(unstable) are. Please, pull request to branch 'v.0' first.
> Create a new branch, suggesting features to the next version, is also accepted. 

## License
[Apache License 2.0](https://github.com/mstr-Wolf/browserBot/blob/master/LICENSE)
