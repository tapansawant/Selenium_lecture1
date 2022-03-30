from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")

driver.maximize_window()  # for maximize window screen
driver.get("https://www.google.com/")
time.sleep(5)
driver.close()
print("test case has successfully completed")