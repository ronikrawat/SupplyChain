from utilites._lib import SeleniumWrapper
from utilites.excel_lib import worksheet


@worksheet("invoice")
class Invoicepage:

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def invoice_page_title(self):
        return self.wrapper.read_text(self.invoice_header)

    def filter_invoice(self, invoice_option="  Invoice Id ", invoice_id="1"):
        self.wrapper.select_item(self.invoice_select, invoice_option)
        self.wrapper.send_text(self.txtInvoiceId, invoice_id)
        self.wrapper.click_element(self.btn_invoice_search)
        self.wrapper.click_element(self.invoice_detail_lnk)

    def check_invoice_detail_page(self):
        return self.wrapper.read_text(self.invoice_detail_pg)
