from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/phptravels/Browsers/chromedriver")

driver.get("http://newtours.demoaut.com/")

assert "Welcome: Mercury Tours" in driver.title
