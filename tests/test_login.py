from POM.login import LoginPage


class Test_Login:

    def test_login(self, pages):
        pages.loginpage.login("admin", "admin123", "Admin")
