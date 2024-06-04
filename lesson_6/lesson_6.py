from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHANGE_TEXT_BUTTON = ("xpath", "//button[@id='populate-text']")
CHANGED_TEXT = ("xpath", "//h2[@id='h2']")

DISPLAY_BUTTON = ("xpath", "//button[@id='display-other-button']")
HIDDEN_BUTTON = ("xpath", "//button[@id='hidden']")

ENABLE_BUTTON = ("xpath", "//button[@id='enable-button']")
DISABLE_BUTTON = ("xpath", "//button[@id='disable']")

ALERT_CALL_BUTTON = ("xpath", "//button[@id='alert']")

driver = webdriver.Chrome()
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

wait = WebDriverWait(driver, 15)

# Task 1
driver.find_element(*CHANGE_TEXT_BUTTON).click()
wait.until(EC.text_to_be_present_in_element(CHANGED_TEXT, "Selenium Webdriver"))

# Task 2
driver.find_element(*DISPLAY_BUTTON).click()
wait.until(EC.visibility_of_element_located(HIDDEN_BUTTON))

# Task 3
driver.find_element(*ENABLE_BUTTON).click()
wait.until(EC.element_to_be_clickable(DISABLE_BUTTON))

# Task 4
driver.find_element(*ALERT_CALL_BUTTON).click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

