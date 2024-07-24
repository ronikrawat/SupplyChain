from selenium import webdriver
from pytest import fixture

from POM.admin import AdminPage
from POM.homepage import Homepage
from POM.login import LoginPage
from POM.manufacturers import Manufacturers
from utilites._lib import SeleniumWrapper

url = r"http://49.249.28.218:8081/AppServer/Supply_Chain_Management/"


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     dest="browser",
                     default="chrome")


@fixture
def driver(request):
    browser = request.config.option.browser
    if browser.upper() == "CHROME":
        _browser = webdriver.Chrome()
    elif browser.upper() == "FIREFOX":
        _browser = webdriver.Firefox()
    elif browser.upper() == "EDGE":
        _browser = webdriver.Edge()
    else:
        raise Exception("Invalid Browser")
    _browser.get(url)
    _browser.maximize_window()
    yield _browser
    _browser.quit()


@fixture
def pages(driver):

    class Page:
        loginpage = LoginPage(driver)
        manufacturer = Manufacturers(driver)
        adminpage = AdminPage(driver)
        homepage = Homepage(driver)
    return Page()
