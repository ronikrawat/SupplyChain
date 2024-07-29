from utilites._lib import SeleniumWrapper
from utilites.excel_lib import worksheet
from ast import literal_eval


@worksheet("retailer")
class Retailerpage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def placeorder(
        self,
        item_quantity,
    ):  # [(item,quantity),(item,quantity)]
        self.wrapper.click_element(self.new_order_lnk)
        price_add = []
        for item, quantity in item_quantity:
            quantity_xpath = str(self.txt_order_quantity).replace("{item}", item)
            self.wrapper.send_text(literal_eval(quantity_xpath), quantity)
            item_price = self.wrapper.read_text(
                literal_eval(str(self.current_price).replace("{item}", item))
            )
            calc_price = self.wrapper.read_text(
                literal_eval(str(self.calculated_price).replace("{item}", item))
            )
            price_add.append((item_price, calc_price))
        self.wrapper.click_element(self.btn_post)
        return price_add

    # def read_total(self):
    #     return self.wrapper.read_text(self.total_price)

    def check_placed_order(self, item_quantity):
        self.driver.get(
            r"http://49.249.28.218:8081/AppServer/Supply_Chain_Management/retailer/view_my_orders.php"
        )
        self.wrapper.click_element(self.my_order_lnk)
        self.wrapper.click_element(self.recent_detail_lnk)
        checkout_order = []
        for item, _ in item_quantity:
            checkout_order.append(
                self.wrapper.read_text(
                    literal_eval(str(self.quantity).replace("{item}", item))
                )
            )
        total = self.wrapper.read_text(self.confirm_total)
        return checkout_order, total

    def check_is_myorder_page(self):
        return self.wrapper.read_text(self.my_order_hdr).strip()
