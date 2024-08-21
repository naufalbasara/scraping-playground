import pandas as pd, time, os, re

from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("auto-open-devtools-for-tabs")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/maps/search/hotels+near+Surabaya,+East+Java/@-7.2941626,112.7677342,13z?entry=ttu')
    time.sleep(10)

    result = {
        'Hotel': [],
        'Harga': [],
        'Rating': [],
        'Link': [],
    }
    no_fetched = 0
    nth_element = 0
    # loop through the scrollable parents
    attempt = 1
    while no_fetched < 200:
        nth_element += 1
        target_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div'
        print(f'Attempt: {attempt}')
        if attempt > 5:
            # scroll if condition met
            time.sleep(5)
            try:
                driver.execute_script("""
                    let parents = document.querySelector('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd');
                    
                    parents.scrollTo(0, parents.scrollHeight);
                """)
            except Exception as error:
                with open('log.txt', 'a') as fl:
                    fl.writelines(f"{datetime.strftime(datetime.now(), format='%D %H:%M:%S')}: [ERROR] {error}\n")
    
        try:
            target_element = driver.find_element(By.XPATH, f'{target_xpath}[{nth_element}]').get_attribute('outerHTML')
            soup = BeautifulSoup(target_element, 'html.parser')
            name = getattr(soup.find('div', class_=['qBF1Pd', 'fontHeadlineSmall', 'kiIehc', 'Hi2drd']), 'text', None)
            price = getattr(soup.find('div', class_='SpFAAb').find_next('div', class_='DJSPJd').find('div', class_=['wcldff', 'fontHeadlineSmall', 'Cbys4b']), 'text', None)
            rating = getattr(soup.find('span', class_='MW4etd'), 'text', None)
            href = soup.find('a', class_='hfpxzc').get('href', None)

            no_fetched += 1
            print(f'{no_fetched}/500')
            print(f'\t{name} ({rating}) {price}/pax  -  {href}')
            result['Hotel'].append(name)
            result['Rating'].append(rating)
            result['Harga'].append(price)
            result['Link'].append(href)
            attempt = 1
        except Exception as error:
            attempt += 1
            with open('log.txt', 'a') as fl:
                fl.writelines(f"{datetime.strftime(datetime.now(), format='%D %H:%M:%S')}: [ERROR] {error}\n")

        if attempt > 10:
            break

    try:
        pd.DataFrame(result).to_excel(os.path.join('../results/hasil_scraping_gmaps.xlsx'))
        pd.DataFrame(result).to_excel(os.path.join('./hasil_scraping_gmaps.xlsx'))
    except:
        pd.DataFrame(result).to_csv(os.path.join('../results/hasil_scraping_gmaps.csv'))
        pd.DataFrame(result).to_csv(os.path.join('./hasil_scraping_gmaps.csv'))