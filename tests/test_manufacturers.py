from utilites.excel_lib import get_test_data_header,get_test_data
from pytest import mark
class Test_Manufacturers:

    login_header = get_test_data_header("testdata","change_m_pass")
    login_data = get_test_data("testdata","change_m_pass")
    filter_header = get_test_data_header("testdata","filter_order")
    filter_data = get_test_data("testdata","filter_order")
    @mark.parametrize(login_header,login_data)
    def test_change_password(self, pages,username,password, user_type, cpassword):
        pages.loginpage.login(username,password, user_type)
        pages.manufacturer._edit_profile()
        actual = pages.manufacturer._change_password(
            password, cpassword, cpassword)
        expected = "Password Updated Successfully"
        assert actual == expected

    @mark.parametrize(login_header,login_data)
    def test_login_Status(self, pages, username,password, user_type, cpassword):
        pages.loginpage.login(username,password, user_type)
        expected = "Welcome sandeep"
        assert expected == pages.homepage.check_login()

    @mark.parametrize(login_header, login_data)
    @mark.parametrize(filter_header,filter_data)
    def test_confirm_order(self, pages, username,password, user_type, cpassword,filter_by,filter_op):
        pages.loginpage.login(username, password, user_type)
        pages.homepage.click_order()
        pages.orderspage.filter_order(filter_by,filter_op)
        expected = "Order is confirmed"
        acctual = pages.orderspage._confirm_order()
        assert expected == acctual, "Not able to perform confirm order"


