from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")

driver.get("http://newtours.demoaut.com/mercurywelcome.php")

# driver.save_screenshot("/Users/echalo/Desktop/screenshots/homepage.png")

driver.get_screenshot_as_file("/Users/echalo/Desktop/screenshots/homepage2.png")
