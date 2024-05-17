from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import csv
import time



driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://healingstreams.tv/zone/BOLGAT')
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.visibility_of_element_located)

with open("data.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:

        driver.find_element( 
            By.XPATH, '//*[@id="my_details"]').send_keys('233')
        
        driver.find_element(
            By.XPATH, '//*[@id="my_details"]').send_keys(line[6])
        
        driver.find_element(By.XPATH,'//*[@id="form2"]/input').send_keys(Keys.ENTER)

        time.sleep(1)

        driver.find_element(
            By.XPATH, '//*[@id="fullname"]').send_keys(line[0])
        

        driver.find_element(
            By.XPATH, '//*[@id="fullname"]').send_keys(' ')
        
        driver.find_element(
            By.XPATH, '//*[@id="fullname"]').send_keys(line[1])
        
       
        wait.until(expected_conditions.visibility_of_element_located)
        
        dropdown = Select(driver.find_element(By.ID,'country1'))

        dropdown.select_by_visible_text("Ghana")
        time.sleep(1)
        
        driver.find_element(By.XPATH,'//*[@id="select2-state1-container"]').click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,'//html/body/span/span/span[1]/input').send_keys('Upper East',Keys.ENTER)
    
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="city2"]').send_keys('Bolgatanga')
        
        driver.find_element(By.XPATH,'//*[@id="need_healing2"]').click()

        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="login"]/input').send_keys(Keys.ENTER)
       
        wait.until(expected_conditions.visibility_of_element_located)

        driver.get('https://healingstreams.tv/zone/BOLGAT')
    
        wait.until(expected_conditions.visibility_of_element_located)
