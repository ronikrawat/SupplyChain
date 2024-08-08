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
    parser.addoption("--headless", action="store_true", dest="headless")


@fixture
def driver(request):
    browser = request.config.option.browser
    _headless = request.config.option.headless
    if browser.upper() == "CHROME":
        options = webdriver.ChromeOptions()
        if _headless:
            options.add_argument('--headless')
        _browser = webdriver.Chrome(options=options)
    elif browser.upper() == "FIREFOX":
        options = webdriver.FirefoxOptions()
        if _headless:
            options.add_argument('--headless')
        _browser = webdriver.Firefox(options=options)
    elif browser.upper() == "EDGE":
        options = webdriver.EdgeOptions()
        if _headless:
            options.add_argument('--headless')
        _browser = webdriver.Edge(options=options)
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
