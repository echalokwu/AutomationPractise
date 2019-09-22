from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/phptravels/Browsers/chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.expedia.com")
driver.find_element(By.XPATH, "//button[@id='tab-flight-tab-hp']").click()
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
time.sleep(3)

driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("09/20/2019")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("09/28/2019")

driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()

# Explicit waits
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='stopFilter_stops-0']")))
element.click()

time.sleep(3)
driver.quit()
