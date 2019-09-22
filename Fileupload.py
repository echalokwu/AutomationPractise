from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()


driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-11").send_keys("/Users/echalo/automation/AutomationPractise"
                                                            "/Downloadedfiles/info.pdf")


