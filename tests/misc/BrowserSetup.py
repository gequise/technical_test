from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.misc import ConfigData


class BrowserSetup:

    def __init__(self):
        options = Options()
        # options.add_argument("--start-maximized") #Windows
        # options.add_argument("--kiosk") #Browser Full Screen
        mobile_emulation = {"deviceName": "iPhone X"}  # Browser Mobile
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome("./drivers/chromedriver_96", options=options)
        self.driver.get(ConfigData.modal_page)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.close()
