import pytest
from base.webdriverFactory import WebDriverFactory

@pytest.yield_fixture()
def setup():
    print("I am in setup function executing before test case")
    yield
    print("I am in setup function executing after test case")

@pytest.yield_fixture(scope="class")
def onetimesetup(request,core_browser):
    wd = WebDriverFactory(core_browser)
    driver = wd.getWebdriverInstance()
    print("I am in onetimesetup function executing before module")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.close()
    print("I am in onetimesetup function executing after module")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def core_browser(request):
    return request.config.getoption("--browser")


