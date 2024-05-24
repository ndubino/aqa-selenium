# Задание 1
# Страница для выполнения задания: https://demoqa.com/text-box
# Действия:
# Заполнить все текстовые поля данными (почистить поля перед заполнением).
# Проверить, что данные действительно введены, используя get_attribute() и assert.
from selenium import webdriver

NAME_FIELD = ["xpath", "//input[@id='userName']"]
EMAIL_FIELD = ["xpath", "//input[@id='userEmail']"]
ADDRESS_FIELD = ["xpath", "//textarea[@id='currentAddress']"]
PERMANENT_FIELD = ["xpath", "//textarea[@id='permanentAddress']"]


driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

driver.find_element(*NAME_FIELD).clear()
driver.find_element(*NAME_FIELD).send_keys("TEST")
assert driver.find_element(*NAME_FIELD).get_attribute("value") == "TEST", "Name field value mismatch"

driver.find_element(*EMAIL_FIELD).clear()
driver.find_element(*EMAIL_FIELD).send_keys("TEST")
assert driver.find_element(*EMAIL_FIELD).get_attribute("value") == "TEST", "Email field value mismatch"

driver.find_element(*ADDRESS_FIELD).clear()
driver.find_element(*ADDRESS_FIELD).send_keys("TEST")
assert driver.find_element(*ADDRESS_FIELD).get_attribute("value") == "TEST", "Address field value mismatch"

driver.find_element(*PERMANENT_FIELD).clear()
driver.find_element(*PERMANENT_FIELD).send_keys("TEST")
assert driver.find_element(*PERMANENT_FIELD).get_attribute("value") == "TEST", "Permanent address field value mismatch"
