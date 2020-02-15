
from base.seleniumdriver import SeleniumDriver


class LoginPo(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _usernametxtbx = "username"
    _pwdtxtbx = "pwd"
    _keepmeloggedinchkbx = "keepLoggedInCheckBox"
    _loginbtn = "//div[contains(text(),'Login')]"

    def usernametxtbx(self,username):
        self.senddata(self._usernametxtbx,"id",username)

    def pwdtxtbx(self,pwd):
        self.senddata(self._pwdtxtbx,"name",pwd)

    def keepmeloggedinchkbx(self):
        self.click(self._keepmeloggedinchkbx,"id")

    def loginbtn(self):
        self.click(self._loginbtn,"xpath")

    def entercredentials(self,username,pwd):
        self.usernametxtbx(username)
        self.pwdtxtbx(pwd)
        self.keepmeloggedinchkbx()
        self.loginbtn()

    def loginpagelanded(self):
        return self.elementisdisplayed(self._usernametxtbx,"id")
