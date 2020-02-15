
import os
from selenium import webdriver


class WebDriverFactory:
    def __init__(self,core_browser):
        self.browser = core_browser
        self.driver_location_chrome = "C:\\Users\\CBT\\PycharmProjects\\AutomationFW\\libs\\chromedriver.exe"
        self.driver_location_firefox = "C:\\Users\\CBT\\PycharmProjects\\AutomationFW\\libs\\geckodriver.exe"
        self.driver_location_ie = "C:\\Users\\CBT\\PycharmProjects\\AutomationFW\\libs\\IEDriverServer.exe"
        os.environ["webdriver.chrome.driver"] = self.driver_location_chrome
        os.environ["webdriver.gecko.driver"] = self.driver_location_firefox
        os.environ["webdriver.ie.driver"] = self.driver_location_ie

    def getWebdriverInstance(self):
        self.driver = None
        baseURl = "http://localhost/login.do"
        if self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=self.driver_location_chrome)
            print("Chrome browser launched")
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=self.driver_location_firefox)
            print("Firefox browser launched")
        else:
            print("Ie browser launched")
            driver = webdriver.Ie(executable_path=self.driver_location_ie)
        driver.get(baseURl)
        driver.implicitly_wait(10)
        return driver
