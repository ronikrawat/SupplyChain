class Test_Manufacturers:

    def test_change_password(self, pages):
        pages.loginpage.login("uuuuuuuu", "uuuuuuuuuu", "Manufacturer")
        pages.manufacturer._edit_profile()
        actual = pages.manufacturer._change_password("uuuuuuuuuu", "xxxxxx", "xxxxxx")
        expected = "Password Updated Successfully"
        assert actual == expected
