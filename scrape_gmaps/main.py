from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
import pandas as pd
import asyncio
from dotenv import load_dotenv
import time

def read_data():
    load_dotenv()
    sheet_id = os.getenv('SHEET_ID')
    url = f'https://docs.google.com/spreadsheets/export?id={sheet_id}&format=xlsx'
    merchants = pd.read_excel(url, sheet_name='Bandung merchant')
    merchants = merchants[['merchant_name', 'address', 'latitude', 'longitude', 'Kecamatan']].values

    return merchants

def save_data(data):
    data_path = os.path.join('./', 'merchant_kecamatan.xlsx')
    pd.DataFrame(data).to_excel(data_path)
    return f'merchant_kecamatan.xlsx saved to current directory'

async def handle(driver):
    driver.switch_to.new_window('tab')
    await asyncio.sleep(1)
    driver.close()

if __name__ == '__main__':
    merchants = read_data()
    sellers_info = []
    num_succeed = 0
    num_failed = 0

    driver = webdriver.Chrome()

    for i in range(len(merchants)):
        time.sleep(2)
        latitude = merchants[i][2]
        longitude = merchants[i][3]

        print(f'Getting {merchants[i][0]} kecamatan data:', end='\t')
        driver.get(f'https://www.google.com/maps/search/{latitude}+{longitude}')
        try:
            element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'DkEaL'))
            )
            driver.implicitly_wait(5)
            text = driver.find_element(By.CLASS_NAME, 'DkEaL').text
            start = re.search(r'(Kecamatan|Kec.) [\w\s]+', text).start()
            end = re.search(r'(Kecamatan|Kec.) [\w\s]+', text).end()
            loc = text[start:end]
            sellers_info.append(
                [merchants[i][0], merchants[i][1], loc]
            )
            print(loc)
            num_succeed += 1
            
            
        except Exception as e:
            sellers_info.append(
                [merchants[i][0], merchants[i][1], None]
            )
            print('failed...')
            num_failed +=1
        
        finally:
            handle(driver)

    driver.quit()
    
    save_data(sellers_info)
    print(f"""
    Statistics:\n\tSuccess Fetch: {num_succeed}\n\tFailed Fetch: {num_failed}
    """)