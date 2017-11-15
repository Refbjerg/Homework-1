from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def Submit_group(self):
        wd = self.wd
        # submit group creation
        wd.find_element_by_name("submit").click()

    def group_creation(self, group):
        # group creation
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)


    def open_homepage(self):
        wd = self.wd
        # open_homepage
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

    def Destroy(self):
        self.wd.quit()
if __name__ == '__main__':
    unittest.main()