from selenium import webdriver
from selenium.webdriver.common.by import By
 
driver = webdriver.Firefox()
# Open Youtube
driver.get("https://www.youtube.com")

login = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button/yt-formatted-string")

login.click()

login = driver.find_element(By.ID, "identifierId")
driver.implicitly_wait(10)
login.send_keys("jamshaid.tahiri1@gmail.com")
login = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
login.click()
login = driver.find_element(By.NAME, "password")
login.send_keys("Muhammad@google.com")





