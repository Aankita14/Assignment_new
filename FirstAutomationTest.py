#Test case
#Open webrowser (chrome/firefox/edge)
#Open URL https://www.saucedemo.com/
#Enter username - standard_user
#Enter password - secret_sauce
#Click on login
#Capture title of the home page(Actual result)
#verify title of the page: Swag Labs(Expected)
#close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

act_title = driver.title
exp_title="Swag Labs"

if act_title == exp_title:
    print("Login Test Pass")
else:
    print("login Test Failed")

driver.close()







