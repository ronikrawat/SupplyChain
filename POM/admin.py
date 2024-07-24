from utilites._lib import SeleniumWrapper
from utilites.excel_lib import worksheet
from ast import literal_eval


@worksheet("admin")
@worksheet("homepage")
@worksheet("manufacturer")
class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def add_manufacturers(self, name, email, phone, username, password):
        self.wrapper.click_element(self.add_manufacturer)
        self.wrapper.send_text(self.manufacturer_name, name)
        self.wrapper.send_text(self.manufacturer_email, email)
        self.wrapper.send_text(self.manufacturer_phone, phone)
        self.wrapper.send_text(self.manufacturer_username, username)
        self.wrapper.send_text(self.manufacturer_password, password)
        self.wrapper.click_element(self.btn_add_manufacturer)

    # Manufacturer Added Successfully
    def confirm_popup(self):
        return self.wrapper.alert_box_text()

    def remove_manufacturer(self, search_data):  # Retailer Deleted Successfully
        xpath = str(self.manufacturer_check)
        newpath = xpath.replace('{search_data}', search_data)
        self.wrapper.click_element(self.nav_manufacturers)
        self.wrapper.click_element(literal_eval(newpath))
        self.wrapper.page_down()
        self.wrapper.click_element(self.manufacturer_delete)
