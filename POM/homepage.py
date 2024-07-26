from utilites._lib import SeleniumWrapper
from utilites.excel_lib import worksheet


@worksheet("homepage")
class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def click_manufacturers(self):
        self.wrapper.click_element(self.nav_manufacturers)

    def click_order(self):
        self.wrapper.click_element(self.nav_orders)

    def click_products(self):
        self.wrapper.click_element(self.nav_products)

    def _logout(self):
        self.wrapper.click_element(self.btn_logout)

    def check_login(self):
        return self.wrapper.read_text(self.welcome_msg).splitlines()[0].strip()
