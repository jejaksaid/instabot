from selenium import webdriver
from time import sleep




class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get("https://instagram.com")
        sleep(2)

InstaBot('username', 'password')


