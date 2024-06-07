import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

SEARCH_FIELD_LOCATOR = ("xpath", "//input[@id='top-s']")
BOOK_LOCATOR = ("xpath", "(//a[contains(text(), '1984')])[1]")
ADD_TO_CART_BUTTON_LOCATOR = ("xpath", "//div[@class='b-product__controls']//button[@type='submit']")

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://oz.by/')

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(SEARCH_FIELD_LOCATOR)
)
search_box.send_keys('1984', Keys.ENTER)

first_item = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(BOOK_LOCATOR)
)
first_item.click()

add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(ADD_TO_CART_BUTTON_LOCATOR)
)
add_to_cart_button.click()

cookies = driver.get_cookies()

driver.delete_all_cookies()
time.sleep(5)

driver.refresh()
time.sleep(5)

for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()

time.sleep(5)