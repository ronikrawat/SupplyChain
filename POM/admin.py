from utilites._lib import SeleniumWrapper
from utilites.excel_lib import worksheet
from ast import literal_eval


@worksheet("admin")
@worksheet("product")
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
        self.wrapper.alert_box_accept()

    def check_manufacturer_added(self, search_data):
        self.wrapper.click_element(self.nav_manufacturers)
        xpath = str(self.manufacturer_check)
        newpath = xpath.replace("{search_data}", search_data)
        return self.wrapper.check_element(literal_eval(newpath))

    # Manufacturer Added Successfully

    def confirm_popup(self):
        return self.wrapper.alert_box_text()

    def remove_manufacturer(self, search_data):  # Retailer Deleted Successfully
        xpath = str(self.manufacturer_check)
        newpath = xpath.replace('{search_data}', search_data)
        self.wrapper.click_element(self.nav_manufacturers)
        self.wrapper.click_element(literal_eval(newpath))
        self.wrapper.click_element(self.manufacturer_delete)

    def add_product(self, name, price, unit, category, stock, description):
        self.wrapper.click_element(self.add_products)
        self.wrapper.send_text(self.product_name, name)
        self.wrapper.send_text(self.product_price, price)
        self.wrapper.select_item(self.unit_dropdown, unit)
        self.wrapper.select_item(self.category_dropdown, category)
        if stock.upper() == "ENABLE":
            self.wrapper.click_element(self.sm_enable)
        elif stock.upper() == "DISABLE":
            self.wrapper.click_element(self.sm_enable)
        else:
            raise Exception("Please choose a valid option")
        self.wrapper.send_text(self.product_discription, description)
        self.wrapper.click_element(self.btn_add_prod)
        self.wrapper.alert_box_accept()

    def check_product(self, search_data):
        self.wrapper.click_element(self.nav_products)
        xpath = str(self.search_product)
        newpath = xpath.replace("{search_data}", search_data)
        return self.wrapper.check_element(literal_eval(newpath))

    def match_product_price(self, search_product, price):
        self.wrapper.click_element(self.nav_products)
        xpath = str(self.p_price)
        newpath = xpath.replace("{search_product}", search_product)
        xpath = newpath.replace("{product_price}", price)
        return self.wrapper.check_element(literal_eval(xpath))

    def edit_product(self, search_data, new_price):
        self.wrapper.click_element(self.nav_products)
        xpath = str(self.search_product)
        newpath = xpath.replace("{search_data}", search_data)
        try:
            self.wrapper.click_element(literal_eval(newpath))
        except TimeoutError:
            raise f"{search_data} Element not found"
        self.wrapper.clear_text(self.product_price)
        self.wrapper.send_text(self.product_price, new_price)
        self.wrapper.click_element(self.sm_enable)
        from time import sleep
        sleep(10)
        self.wrapper.click_element(self.btn_update)
        # self.wrapper.send_text(self.p_price, new_price)
        # self.wrapper.click_element(self.btn_update)
        self.wrapper.alert_box_accept()

