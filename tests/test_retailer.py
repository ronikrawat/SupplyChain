from pytest import mark
from utilites.excel_lib import get_test_data, get_test_data_header


class TestRetailer:
    header_login = get_test_data_header("testdata", "retailer_login")
    data_login = get_test_data("testdata", "retailer_login")
    retailer_header = get_test_data_header("testdata", "retailer_sys")
    retailer_data = get_test_data("testdata", "retailer_sys")

    @mark.parametrize(header_login, data_login)
    @mark.parametrize(retailer_header, retailer_data)
    def test_place_order(
            self,
            pages,
            item_quantity,
            q_list,
            total,
            quantity_list,
            f_total,
            username,
            password,
            user_type,
    ):
        pages.loginpage.login(username, password, user_type)
        item_quantity = eval(item_quantity)
        result = pages.retailerpage.placeorder(item_quantity)
        assert result == eval(
            quantity_list
        ), f"Price should be {quantity_list} but it is {result}"
        # assert t_total == int(total), f"Total is {result} but it should be {int(total)}"
        # assert "My Orders" == pages.retailerpage.check_is_myorder_page(), "This is not 'My Order' page"
        quantity, final_total = pages.retailerpage.check_placed_order(item_quantity)
        assert eval(q_list) == quantity, f"Quantity is {quantity} it should be {q_list}"
        assert (
                f_total == final_total
        ), f"Final total is {final_total} it should be {f_total}"
        pages.homepage._logout()
