from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")

driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")

driver.find_element_by_xpath("//input[@id='btnLogin']").click()

maintenance = driver.find_element_by_xpath("//b[text()='Maintenance']")
purgeRecords = driver.find_element_by_xpath("//a[text()='Purge Records']")
employeeRecords = driver.find_element_by_id("menu_maintenance_purgeEmployee")

actions = ActionChains(driver)
actions.move_to_element(maintenance).move_to_element(purgeRecords).move_to_element(employeeRecords).click().perform()
time.sleep(5)


