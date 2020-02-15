import pytest
from pages.loginpo import LoginPo
from pages.homepo import HomePo

@pytest.mark.usefixtures("setup","onetimesetup")
class Test_CreateUser:
    @pytest.fixture(autouse=True)
    def classsetup(self):
        self.lp =LoginPo(self.driver)
        self.hp = HomePo(self.driver)


    @pytest.mark.run(order=1)
    def test_createusersuccessfully(self):
        self.lp.entercredentials("admin","manager")
        #add steps here
        self.hp.logoutbtn()
