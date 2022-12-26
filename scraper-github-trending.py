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
driver.implicitly_wait(10000)
driver.maximize_window()
r=1
templist = []

while(r<3):
    try:
        method=driver.find_element(By.CLASS_NAME, 'company_title').text
        Desc=driver.find_element(By.CLASS_NAME, 'company_title').text
        Table_dict={ 'Method': method,'Description':Desc}
        templist.append(Table_dict)
        df = pd.DataFrame(templist)
        r += 1
        print(df)		
    except NoSuchElementException:
        break
		
# saving the dataframe to a csv
df.to_csv('table.csv')
driver.close()
