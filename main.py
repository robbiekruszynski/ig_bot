from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

driver.get('https://www.instagram.com/')

wait.until(ec.element_to_be_clickable((By.NAME, "username"))).send_keys("mr.percys_palace")
el = wait.until(ec.element_to_be_clickable((By.NAME, "password")))
el.send_keys("D3arpercy")
el.send_keys(Keys.ENTER)

sleep(5)

driver.close()