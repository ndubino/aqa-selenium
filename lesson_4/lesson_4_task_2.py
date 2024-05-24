# Страница для выполнения задания: https://the-internet.herokuapp.com/login
# Данные для входа:
# Логин: tomsmith
# Пароль: SuperSecretPassword!
# Действия:
# Заполнить все поля формы данными (почистить поля перед заполнением).
# Нажать на кнопку "Login".
# Проверить, что вы авторизовались. Можно проверить, что кнопка logout отображается на странице,
# а кнопка логина исчезла (но тут придется погуглить про try, except) изучим его позже.

from selenium import webdriver

USERNAME_FIELD = ("xpath", "//input[@id='username']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
LOGOUT_BUTTON = ("xpath", "//i[@class='icon-2x icon-signout']")


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(*USERNAME_FIELD).clear()
driver.find_element(*USERNAME_FIELD).send_keys("tomsmith")

driver.find_element(*PASSWORD_FIELD).clear()
driver.find_element(*PASSWORD_FIELD).send_keys("SuperSecretPassword!")


driver.find_element(*SUBMIT_BUTTON).click()

try:
    logout_button = driver.find_element(*LOGOUT_BUTTON)
    submit_button = driver.find_elements(*SUBMIT_BUTTON)
    if logout_button.is_displayed() and not submit_button:
        print("Successful")
    else:
        print("Failed")
except Exception as e:
    print(f"Login failed with error: {e}")
