from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# Scroll down page by pixel
# driver.execute_script("window.scrollBy(0, 500)", "")

# Scroll down page till the element is visible
# flag = driver.find_element_by_xpath("//td[contains(text(),'India')]")
# driver.execute_script("arguments[0].scrollIntoView();", flag)


# Scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
