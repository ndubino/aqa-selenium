import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://hyperskill.org/login')

driver.switch_to.new_window("tab")
driver.get('https://www.avito.ru/')


driver.switch_to.new_window("tab")
driver.get('https://www.ozon.ru/')


driver.switch_to.window(driver.window_handles[0])
title_1 = driver.title

driver.switch_to.window(driver.window_handles[1])
title_2 = driver.title

driver.switch_to.window(driver.window_handles[2])
title_3 = driver.title

print(f"{title_1}\n{title_2}\n{title_3}")

driver.switch_to.window(driver.window_handles[0])
driver.find_element("xpath", "//nav//button[text()='Start for free']").click()

driver.switch_to.window(driver.window_handles[1])
driver.find_element("xpath", "//div//*[@data-icon='favorites-filled']").click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[2])
driver.find_element("xpath", "//a[@data-widget='favoriteCounter']").click()
time.sleep(5)



