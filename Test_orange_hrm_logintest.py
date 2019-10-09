import unittest
from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver import ActionChains
import time

"""
Test case: OraneHRM login test
---
1) Launch browser
2) Open URL
3) Verify home page title
4) Verify login
5) Close browser
"""


class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Start we browser"""
        cls.driver = webdriver.Chrome(
            executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        """Stop we browser"""
        cls.driver.quit()
        cls.driver.close()
        print("Test Completed")

    def test_case_01(self):
        """Verify homepage title"""
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")
        print(self.driver.title)

    # def test_case_02(self):
    #     """Verify Login and Homepage title"""
    #     self.driver.get("https://opensource-demo.orangehrmlive.com")
    #     self.driver.find_element_by_name("txtUsername").send_keys("Admin")
    #     self.driver.find_element_by_name("txtPassword").send_keys("admin123")
    #     self.driver.find_element_by_name("Submit").click()
    #     time.sleep(5)
    #     self.driver.find_element_by_id("welcome").click()
    #     self.driver.find_element_by_xpath("//a[text()='Logout']").click()

    # def test_case_03(self):
    #     """Add employee"""
    #     self.driver.get("https://opensource-demo.orangehrmlive.com")
    #     self.driver.find_element_by_name("txtUsername").send_keys("Admin")
    #     self.driver.find_element_by_name("txtPassword").send_keys("admin123")
    #     self.driver.find_element_by_name("Submit").click()
    #     PIM = self.driver.find_element_by_id("menu_pim_viewPimModule")
    #     EmployeeList = self.driver.find_element_by_id("menu_pim_viewEmployeeList")
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(PIM).move_to_element(EmployeeList).click().perform()
    #     time.sleep(5)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Reports'))
