from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(executable_path ='/usr/lib/chromium-browser/chromedriver')
driver.get('https://clutch.co/agencies/digital-design?geona_id=26303&related_services=field_pp_sl_web_programming&related_services=field_pp_sl_app_interface_design&related_services=field_pp_sl_digital_strategy&related_services=field_pp_sl_web_design')
driver.implicitly_wait(100)
scraped_companies = []
company_titles = driver.find_elements(By.CLASS_NAME, 'company_title')
r=0
while r<100:
    for title in company_titles:
        scraped_companies.append(title.text)
        print(title.text)
        r+=1
		
df = pd.DataFrame(scraped_companies)
df.to_csv('table.csv')
driver.close()
