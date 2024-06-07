import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920, 1080")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                     'AppleWebKit/537.36 (KHTML, like Gecko)'
                     'Chrome/58.0.3029.110 Safari/537.3')

driver = webdriver.Chrome(options=options)

# Task 1

driver.get("https://www.google.com/")

cookie = {
    'name': 'username',
    'value': 'user123'
}

driver.add_cookie(cookie)
time.sleep(10)

driver.refresh()
time.sleep(10)

cookie = driver.get_cookie('username')
assert cookie['value'] == 'user123', "Failed"
print("ok")

# Task 2
driver.get('https://www.google.com/')

cookie = {
    'name': 'username',
    'value': 'user123'
}
driver.add_cookie(cookie)

driver.refresh()
assert driver.get_cookie('username')
driver.delete_cookie('username')
driver.refresh()
cookie = driver.get_cookie('username')
assert cookie is None, "FAILED"
print("ok")
