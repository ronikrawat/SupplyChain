from utilites.excel_lib import get_test_data, get_test_data_header
from pytest import mark


class Test_Login:
    header = get_test_data_header("testdata", "test_login")
    data = get_test_data("testdata", "test_login")
    new = header.split(",")

    @mark.parametrize(header, data)
    def test_login(self, pages, username, password, user_type):
        pages.loginpage.login(username, password, user_type)
