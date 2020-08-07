from selenium import webdriver

class Webdriver(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def chrome(self):
        chrome = webdriver.Chrome(self.driver)
        chrome.get(self.url)
        chrome.maximize_window()
        chrome.save_screenshot("screenshots\\01-browser.png")
        return chrome
