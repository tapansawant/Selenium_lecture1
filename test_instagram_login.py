from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")

driver.maximize_window()  # for maximize window screen
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.find_element_by_name("username").send_keys("_tapan__45")
time.sleep(1)
driver.find_element_by_name("password").send_keys("")
time.sleep(1)
#driver.find_element_by_class_name().click()

time.sleep(5)
driver.close()
print("test case has successfully completed")

