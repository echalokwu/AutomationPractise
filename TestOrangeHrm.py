from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")

driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")

driver.find_element_by_xpath("//input[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//b[contains(text(),'Admin')]")
usermgnt = driver.find_element_by_xpath("//a[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()
