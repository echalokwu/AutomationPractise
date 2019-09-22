from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_css_selector("#HTML9 > div:nth-child(2) > button:nth-child(1)").click()

time.sleep(5)

# driver.switch_to.alert.accept() # Closes alert window using OK button


driver.switch_to.alert.dismiss()   # Closes alert window using CANCEL button
