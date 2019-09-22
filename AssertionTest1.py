import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    # def testName1(self):
    #     driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")
    #     driver.get("https://google.com")
    #     titleOfWebPage = driver.title
    #     self.assertEqual("Google123", titleOfWebPage, "webpage title is not same")
    #     # self.assertNotEqual("Google123", titleOfWebPage, "webpage title is not same")
    #
    # def testName2(self):
    #     driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")
    #     driver.get("https://google.com")
    #     titleOfWebPage = driver.title
    #     # self.assertTrue(titleOfWebPage == "Google")  # True
    #     self.assertFalse(titleOfWebPage == "Google123")
    #
    # def testName2(self):
    #     driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")
    #     # driver = None
    #     # self.assertIsNone(driver)
    #     self.assertIsNotNone(driver)

    def testName2(self):
        list = {"python", "selenium", "java"}
        self.assertIn("python", list)


if __name__ == "__main__":
    unittest.main()
