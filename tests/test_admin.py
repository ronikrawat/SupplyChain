from POM.admin import AdminPage


class Test_Admin:

    def test_add_manufacturer(self, pages):
        pages.loginpage.login("admin", "admin123", "Admin")
        pages.adminpage.add_manufacturers(
            "uuuuu", "uuuuu@gmail.com", "8888888888", "uuuuuuuu", "uuuuuuuuuu")
        expected_message = "Manufacturer Added Successfully"
        assert expected_message == pages.adminpage.confirm_popup(), f"Expected value [{expected_message}] is not same as actual value [{pages.adminpage.add_manufacturers_confirm_popup()}]"

    def test_delete_manufacturer(self, pages, search_data="uuuuu@mail.com"):
        pages.loginpage.login("admin", "admin123", "Admin")
        pages.homepage.click_manufacturers()
        pages.adminpage.remove_manufacturer(search_data)
        expected_result = "manufacturers Deleted Successfully"
        assert expected_result == pages.adminpage.confirm_popup()
