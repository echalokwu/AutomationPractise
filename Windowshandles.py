from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/phptravels/Browsers/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//a[@href='http://www.sakinalium.in']//button[@class='btn btn-info'][contains(text(),"
                             "'click')]").click()

print(driver.current_window_handle)  # CDwindow-3B107BB7E6865D70BB41FDD70BACCE65

handles = driver.window_handles  # returns all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()
