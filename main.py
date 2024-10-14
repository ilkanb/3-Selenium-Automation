from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

#Define driver,options and service
chrome_options = Options()
chrome_options.add_argument("--disable-serach-engine-choice-screen")

download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)


service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)

#Load Webpages
driver.get('http://demoqa.com/login')

# Locate username,password and button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

#fill the spaces and click button
user_name = os.getenv("SELENIUM_NAME")
user_password = os.getenv("SELENIUM_PASSWORD")
username_field.send_keys(user_name)
password_field.send_keys(user_password)
driver.execute_script("arguments[0].click();",login_button)

#click elements and textbox
elements = (WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

##Form Filler Check

fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_adress_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_adress_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

#Fill in the form fields

fullname_field.send_keys('John Smith')
email_field.send_keys('john@gmail.com')
current_adress_field.send_keys('John Street 100, New York, USA')
permanent_adress_field.send_keys('John Street 100, New York, USA')
driver.execute_script("arguments[0].click()", submit_button)

#download

download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
download.click()
download_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'downloadButton')))
download_button.click()

input("Press Enter to Close App")
driver.quit()
