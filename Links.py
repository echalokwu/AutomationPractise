from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/phptravels/Browsers/chromedriver")

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME, "a")

print(len(links))

for links in links:
    print(links.text)

