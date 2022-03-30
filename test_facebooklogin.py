from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")

driver.maximize_window()  # for maximize window screen
driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjQ4NjM1NzYwLCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D")
time.sleep(1)
driver.find_element_by_name("email").send_keys("tapansawant45@gmail.com")
time.sleep(1)
driver.find_element_by_name("pass").send_keys("")
time.sleep(1)
driver.find_element_by_name("login").click()

time.sleep(5)
driver.close()
print("test case has successfully completed")

