from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)



    def open_home_page(self):
        wd = self.wd
        # open_homepage
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

    def Destroy(self):
        self.wd.quit()




if __name__ == '__main__':
    unittest.main()