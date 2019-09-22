from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("prefs", {"download.default_directory": "/Users/echalo/Desktop/Downloadedfiles"})

driver = webdriver.Chrome(executable_path="/Users/echalo/automation/AutomationPractise/drivers/chromedriver",
                          options=options)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

# Download text file
driver.find_element_by_id("textbox").send_keys("testing download text file")
driver.find_element_by_id("createTxt").click()  # Generate file button
driver.find_element_by_id("link-to-download").click()  # Download link
time.sleep(3)


# Download pdf file

driver.find_element_by_id("pdfbox").send_keys("testing pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(3)


driver.close()