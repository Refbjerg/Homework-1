# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Homework1(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_Homework1(self):
        success = True
        wd = self.wd
        self.open_homepage(wd)
        #login
        self.login(wd, "Admin", "secret")
        self.group_creation(wd)
        self.Submit_group(wd)
        self.assertTrue(success)

    def Submit_group(self, wd):
        # submit group creation
        wd.find_element_by_name("submit").click()

    def group_creation(self, wd):
        # group creation
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Group-1")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("Groupleader")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("Groupfooter")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_homepage(self, wd):
        # open homepage
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
