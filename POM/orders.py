from selenium.common import InvalidElementStateException

from utilites._lib import SeleniumWrapper
from utilites.excel_lib import worksheet


@worksheet("order")
@worksheet("homepage")
class Orderspage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def filter_order(self, filter_by, filter_op):
        self.wrapper.select_item(self.order_filter_dropdown, filter_by)
        self.wrapper.select_item(self.order_status_dropdown, filter_op)
        self.wrapper.click_element(self.search_order)

    def _confirm_order(self):
        self.wrapper.click_element(self.nav_orders)

        self.wrapper.click_element(self.confirm_order)
        try:
            return self.wrapper.alert_box_text()
        except:
            return "Not able to Confirm the order"
