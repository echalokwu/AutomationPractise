from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")

driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")

driver.find_element_by_xpath("//input[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//b[contains(text(),'Admin')]")
maintenance = driver.find_element_by_xpath("//b[text()='Maintenance']")
purgeRecords = driver.find_element_by_xpath("//a[text()='Purge Records']")
employeeRecords = driver.find_element_by_id("menu_maintenance_purgeEmployee")
job = driver.find_element_by_id("menu_admin_Job")
jobtitle = driver.find_element_by_xpath("//a[text()='Job Titles']")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(job).move_to_element(jobtitle).click().perform()
time.sleep(5)

FinanceManager = driver.find_element_by_id("ohrmList_chkSelectRecord_5")
SoftwareQA = driver.find_element_by_id("ohrmList_chkSelectRecord_10")

FinanceManager.click()
SoftwareQA.click()
time.sleep(5)

driver.close()

