from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")

driver.maximize_window()  # for maximize window screen
driver.get("https://www.google.com/")
time.sleep(1)
driver.find_element_by_name("q").send_keys("harman")  #it will search q element which is our search bar and we r searching harman
time.sleep(1)
driver.find_element_by_name("btnK").click()
time.sleep(5)  # 5 min chrome chalel
driver.close()
print("test case has successfully completed")

