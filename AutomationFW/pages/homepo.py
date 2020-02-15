from base.seleniumdriver import SeleniumDriver


class HomePo(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    _logoutlink = "logoutLink"
    _timetrack_title = "//div[contains(text(),'TIME-TRACK')]"



    def logoutbtn(self):
        self.click(self._logoutlink,"id")

    def homepagelanded(self):
        self.waitforvlisbleofelement(self._timetrack_title,"xpath",60,20)
        return self.gettitle()
