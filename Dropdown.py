from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/phptravels/Browsers/chromedriver")

driver.get("https://fs2.formsite.com/meherpaven/forms2/index.html?1537702596407")

element = driver.find_element_by_id("xddddddd")
drp = Select(element)
drp.select_by_value()
drp.select_by_index()
drp.select_by_visible_text()
