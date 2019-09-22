from selenium import webdriver
import unittest


class SearchEngineTest(unittest.TestCase):

    def test_Google(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")
        self.driver.get("https://www.google.com")
        print("Title of the page is:" + self.driver.title)
        self.driver.close()

    @unittest.SkipTest
    def test_Bing(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")
        self.driver.get("https://bing.com")
        print("Title of the page is:" + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
