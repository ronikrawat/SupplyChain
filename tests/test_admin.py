from utilites.excel_lib import get_test_data_header, get_test_data
from pytest import mark


class Test_Admin:
    admin_header = get_test_data_header("testdata", "admin_login")
    admin_data = get_test_data("testdata", "admin_login")
    add_manufacturer_header = get_test_data_header("testdata", "test_add_manufacturer")
    add_manufacturer_data = get_test_data("testdata", "test_add_manufacturer")
    add_product_header = get_test_data_header("testdata", "add_product")
    add_product_data = get_test_data("testdata", "add_product")
    search_product_header = get_test_data_header("testdata", "search_product")
    search_product_price = get_test_data("testdata", "search_product")
    edit_product_header = get_test_data_header("testdata", "edit_product")
    edit_product_data = get_test_data("testdata", "edit_product")

    @mark.parametrize(admin_header, admin_data)
    @mark.parametrize(add_manufacturer_header, add_manufacturer_data)
    def test_add_manufacturer(
        self,
        pages,
        username,
        password,
        user_type,
        name,
        email,
        phone,
        m_username,
        m_password,
    ):
        pages.loginpage.login(username, password, user_type)
        pages.adminpage.add_manufacturers(name, email, phone, m_username, m_password)
        value = email
        assert True == pages.adminpage.check_manufacturer_added(
            value
        ), f"{value} is not found"
        # expected_message = "Manufacturer Added Successfully"
        # assert expected_message == pages.adminpage.confirm_popup(), \
        #     (f"Expected value [{expected_message}] is not same as actual value "
        #      f"[{pages.adminpage.add_manufacturers_confirm_popup()}]")

    def test_delete_manufacturer(self, pages, search_data="uuuuu@gmail.com"):
        pages.loginpage.login("admin", "admin123", "Admin")
        pages.homepage.click_manufacturers()
        pages.adminpage.remove_manufacturer(search_data)
        expected_result = "manufacturers Deleted Successfully"
        assert expected_result == pages.adminpage.confirm_popup()

    @mark.parametrize(add_product_header, add_product_data)
    @mark.parametrize(admin_header, admin_data)
    @mark.parametrize(search_product_header, search_product_price)
    @mark.parametrize(edit_product_header, edit_product_data)
    def test_add_product(
        self,
        pages,
        name,
        price,
        unit,
        category,
        stock,
        description,
        search_data,
        product_price,
        update_product,
        update_price,
        username,
        password,
        user_type,
    ):
        pages.loginpage.login(username, password, user_type)
        pages.adminpage.add_product(name, price, unit, category, stock, description)
        assert True == pages.adminpage.check_product(
            search_data
        ), f"Product {search_data} not found"
        print((update_product, update_price, "c" * 50))
        pages.adminpage.edit_product(update_product, update_price)
        assert True == pages.adminpage.match_product_price(
            update_product, product_price
        ), f"{update_product} is not in the list"
