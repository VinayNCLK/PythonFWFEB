import pytest
from pages.loginpo import LoginPo
from pages.homepo import HomePo
from base.seleniumdriver import SeleniumDriver

@pytest.mark.usefixtures("setup","onetimesetup")
class Test_Login:
    @pytest.fixture(autouse=True)
    def classsetup(self):
        self.lp =LoginPo(self.driver)
        self.hp = HomePo(self.driver)
        print("I am in classsetup function executing before test case")

    @pytest.mark.run(order=1)
    def test_validatesuccessfulllogin(self):
        try:
            assert self.lp.loginpagelanded() == True
            self.lp.entercredentials("admin","manager")

            assert self.hp.homepagelanded() == "atiTIME - Enter Time-Track"
            self.hp.logoutbtn()
        except Exception as e:
            #self.getscreenshot("validatesuccessfulllogin")
            self.driver.save_screenshot("screenshots\\validatesuccessfullloginfailure.png")
            raise Exception