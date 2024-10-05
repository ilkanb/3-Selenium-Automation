from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--disable-serach-engine-choice-screen")

#Define driver,options and service
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)

#Load Webpage
driver.get('http://demoqa.com/login')

# Locate username,password and button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

#fill the spaces and click button
username_field.send_keys('ilkanb')
password_field.send_keys('Kokarcorap12.3$')
driver.execute_script("arguments[0].click();",login_button)



input("Press Enter to Close App")
driver.quit()