from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/selectable")

GRID_TAB_LOCATOR = ("xpath", "//a[@id='demo-tab-grid']")
ONE_BOX_LOCATOR = ("xpath", f"//li[text()='One']")
TWO_BOX_LOCATOR = ("xpath", f"//li[text()='Two']")
THREE_BOX_LOCATOR = ("xpath", f"//li[text()='Three']")


driver.find_element(*GRID_TAB_LOCATOR).click()

one_box = driver.find_element(*TWO_BOX_LOCATOR)
one_box.click()
assert "activ" in one_box.get_attribute("class")

two_box = driver.find_element(*ONE_BOX_LOCATOR)
two_box.click()
assert "activ" in two_box.get_attribute("class")

three_box = driver.find_element(*THREE_BOX_LOCATOR)
three_box.click()
assert "activ" in three_box.get_attribute("class")

one_box.click()
assert "activ" not in one_box.get_attribute("class")

two_box.click()
assert "activ" not in two_box.get_attribute("class")

three_box.click()
assert "activ" not in three_box.get_attribute("class")


