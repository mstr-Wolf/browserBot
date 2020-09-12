from selenium import webdriver

def open_url(request_URL):
    browser = webdriver.Chrome("/bin/chromedriver")
    browser.get(request_URL)