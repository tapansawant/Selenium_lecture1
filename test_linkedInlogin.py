from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")

driver.maximize_window()

driver.get("https://www.google.com/")
time.sleep(2)
driver.find_element_by_name("q").send_keys("LinkedIn")
time.sleep(1)
driver.find_element_by_name("btnK").click()
time.sleep(1)
driver.find_element_by_partial_link_text("LinkedIn Login, Sign in").click()
time.sleep(1)
driver.find_element_by_id("username").send_keys("")
time.sleep(1)
driver.find_element_by_id("password").send_keys("")
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(8)
driver.close()

print("Test case ran successfully")
