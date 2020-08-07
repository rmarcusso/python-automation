from selenium import webdriver

class authentication(object):
    def __init__(self, chrome, username, password):
        self.chrome = chrome
        self.username = username
        self.password = password

    def auth(self):
        self.chrome.find_element_by_id('user-name').send_keys(self.username)
        self.chrome.find_element_by_id('password').send_keys(self.password)
        self.chrome.save_screenshot("screenshots\\02-authentication.png")
        self.chrome.find_element_by_class_name("btn_action").click()
        self.chrome.save_screenshot("screenshots\\03-authentication_success.png")
