#!/usr/bin/python

import datetime
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException


count = 5
file_path = 'C:\\Users\\user\\Downloads\\step2_big5.txt'

date_list = []
weather_list = []
temp_low_list = []
temp_high_list = []

time_id_list = [
    'PC7_Wx PC7_D1 PC7_D1D', 
    'PC7_Wx PC7_D2 PC7_D2D', 
    'PC7_Wx PC7_D3 PC7_D3D', 
    'PC7_Wx PC7_D4 PC7_D4D', 
    'PC7_Wx PC7_D5 PC7_D5D'
]

high_temp_id_list = [
    'PC7_MaxT PC7_D1 PC7_D1D', 
    'PC7_MaxT PC7_D2 PC7_D2D', 
    'PC7_MaxT PC7_D3 PC7_D3D', 
    'PC7_MaxT PC7_D4 PC7_D4D', 
    'PC7_MaxT PC7_D5 PC7_D5D'
]

low_temp_id_list = [
    'PC7_MinT PC7_D1 PC7_D1D', 
    'PC7_MinT PC7_D2 PC7_D2D', 
    'PC7_MinT PC7_D3 PC7_D3D', 
    'PC7_MinT PC7_D4 PC7_D4D', 
    'PC7_MinT PC7_D5 PC7_D5D'
]

def get_weather_forecast():
    # Open website with Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)

    try:
        browser.get('https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6600100')
        time.sleep(5)
        
        browser.find_element_by_id('Tab_weeksTable').click()
        time.sleep(5)

        # Get website html info with BeautifulSoup
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        table = soup.find('table', {'id': 'TableIdweeks'})

        # Get date
        for i in range(count):
            date = (datetime.date.today() + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
            date_list.append(date)

        # Get weather
        for time_id in time_id_list:
            element_headers = table.find('td', {'headers' : time_id}).find_all('img')
            for element in element_headers:
                weather_title = element.get('title')
                weather_list.append(weather_title)

        # Get high temp
        for high_temp_id in high_temp_id_list:
            element_headers = table.find('td', {'headers' : high_temp_id}).find_all('span', {'class' : 'tem-C is-active'})
            for element in element_headers:
                temp_high_list.append(int(element.text))

        # Get low temp
        for low_temp_id in low_temp_id_list:
            element_headers = table.find('td', {'headers' : low_temp_id}).find_all('span', {'class' : 'tem-C is-active'})
            for element in element_headers:
                temp_low_list.append(int(element.text))

        status = 'sucessful'
        return status

    except WebDriverException:
        time.sleep(5)
    
        status = 'failed'
        return status

    finally:
        browser.close()

if __name__ == "__main__":
    connect_count = 0

    datetime_dt = datetime.datetime.today()# 獲得當地時間
    datetime_str = datetime_dt.strftime("%Y/%m/%d")
    
    # Check temp file exist or not
    if os.path.exists(file_path):
        with open(file_path) as f:
            lines = f.read() # File has many lines
            first = lines.split('\n', 1)[0] # Just read first line
            first = first.replace('date1=', '')
        
        while (datetime_str != first): # Check info update
            status = get_weather_forecast()
            connect_count += 1
            
            if status == 'sucessful':
                break
            elif (connect_count == 5):
                break
            else:
                break
    else:
        # Get weather info
        status = get_weather_forecast()
        
        while status == 'failed' :
            get_weather_forecast()
            connect_count += 1
            
            if status == 'sucessful':
                break
            elif (connect_count == 5):
                break
            else:
                break

    # Make file
    text = open(file_path, 'w')

    for i in range(count):
        text.write('date' + str(i+1) + '=' + str(date_list[i]) + '\n')

    for i in range(count):
        text.write('Temp' + str(i+1) + '=' + str(weather_list[i]) + '\n')

    for i in range(count):
        text.write('statusl' + str(i+1) + '=' + str(temp_low_list[i]) + '\n' )

    for i in range(count):
        text.write('statush' + str(i+1) + '=' + str(temp_high_list[i]) + '\n' )

    text.close()
