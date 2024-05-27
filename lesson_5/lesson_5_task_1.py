import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

UPLOAD_FILE = "//input[@type='file']"
file_to_upload = os.path.join(os.getcwd(), "Python.svg.png")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")

upload_element = driver.find_element(By.XPATH, UPLOAD_FILE)
upload_element.send_keys(file_to_upload)
time.sleep(5)


