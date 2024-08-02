from selenium import webdriver
from pytest import fixture

from POM.admin import AdminPage
from POM.homepage import Homepage
from POM.invoice import Invoicepage
from POM.login import LoginPage
from POM.manufacturers import Manufacturers
from POM.orders import Orderspage
from POM.retailer import Retailerpage

url = r"http://xxxxxxxxxxxxxxx/AppServer/Supply_Chain_Management/" #confidential


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", dest="browser", default="chrome")


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
        orderspage = Orderspage(driver)
        invoicepage = Invoicepage(driver)
        retailerpage = Retailerpage(driver)

    return Page()
