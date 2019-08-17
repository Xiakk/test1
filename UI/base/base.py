from selenium import webdriver
import threading

class Driver:
    def __init__(self):
        self.brower = webdriver.chrome()

    def open_brower(self, name1, name2):

        self.brower.maximize_window()
