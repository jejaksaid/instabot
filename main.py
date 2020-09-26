from selenium import webdriver
from time import sleep
from password  import pw 

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get("https://instagram.com")
        sleep(2)

InstaBot('msaid_r', 'password')


