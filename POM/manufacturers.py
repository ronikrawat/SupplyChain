from utilites._lib import SeleniumWrapper
from utilites.excel_lib import worksheet


@worksheet("manufacturer")
class Manufacturers:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(driver)

    def _edit_profile(self):
        self.wrapper.click_element(self.edit_profile)

    def _change_password(self, old, new, cpass):
        self.wrapper.click_element(self.manufacturer_change_password)
        self.wrapper.send_text(self.manufacturer_old_password, old)
        self.wrapper.send_text(self.manufacturer_new_password, new)
        self.wrapper.send_text(self.manufacturer_confirm_password, cpass)
        self.wrapper.click_element(self.manufacturer_change_password)
        return self.wrapper.alert_box_text()
