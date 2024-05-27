import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

project_root = os.path.dirname(os.path.abspath(__file__))

download_dir = os.path.join(os.getcwd(), 'downloads')
options = Options()
options.add_experimental_option("prefs", {"download.default_directory": download_dir})

driver = webdriver.Chrome(options=options)

driver.get("http://the-internet.herokuapp.com/download")

for link in driver.find_elements(By.XPATH, "//div[@class='example']/a"):
    link.click()
    time.sleep(1)

driver.quit()
