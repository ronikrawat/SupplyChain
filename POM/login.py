from utilites.excel_lib import worksheet
from utilites._lib import SeleniumWrapper


@worksheet("login")
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def login(self, username, password, user_type):
        self.wrapper.send_text(self.txt_username, username)
        self.wrapper.send_text(self.txt_password, password)
        self.wrapper.select_item(self.select_type, user_type)
        self.wrapper.screenshot()
        self.wrapper.click_element(self.login_btn)
        self.wrapper.screenshot()
