import pandas as pd, os, time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

def get_cookie(cookie_str):
    cookie_dict = {}
    
    cookies = cookie_str.split(';')
    for cookie in cookies:
        try:
            cookie_key, cookie_val = cookie.split('=')
            cookie_dict[cookie_key.strip()]=cookie_val.strip()
        except Exception as error:
            print(f"{datetime.strftime(datetime.now(), format='%D %H:%M:%S')}: [ERROR] {error}")

    print("Cookie set.")
    return cookie_dict

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("auto-open-devtools-for-tabs")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.traveloka.com/')
    cookie_dict = driver.get_cookies()

    # cookie_dict = get_cookie('_cs_c=1; _tt_enable_cookie=1; _ttp=wf_04jN6zQ8mDdkP9A3l6PEooZ5; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22yjErpLJptowiVkHxmYYA%22%7D; __rtbh.uid=%7B%22id%22%3A%22undefined%22%2C%22eventType%22%3A%22uid%22%7D; g_state={"i_p":1711858857191,"i_l":2}; __gads=ID=98487c5770a3de03:T=1711775866:RT=1711775866:S=ALNI_Mb2cpAjgd4bWK7ZHH4EqNNOBCyXSA; __gpi=UID=00000d780654e21f:T=1711775866:RT=1711775866:S=ALNI_Ma-G-F62m1PMeWpsM-9QzR_2bCyQw; __eoi=ID=76cb21f7adbdcf97:T=1711775866:RT=1711775866:S=AA-Afjb3jL6URl3hCg5o20jxAT5o; amp_f4354c=vxZtFe7r_gpqqKy5EBDBRV...1hrr2rrmm.1hrr2rsj1.0.5.5; _cs_id=731462f4-fd05-ad47-dad6-1c9b646c298f.1710142471.3.1713527191.1713527191.1.1744306471906.1; cto_bundle=ugqWCF90bm5oZlZEanRpTnRlRUt3eGtvZnI3QXRicVVJRHRJT1U2emNmJTJCa3pPdWFXaWlGbVdvS1l3QUtmZGhCdlpIU2FDMllTR1dpRFFRTyUyRmtPc3A1dEFoYm5RS09wN1dvbiUyQk03UTFhQmhXRE5LUXViSGIzVGRVbGx6NUklMkZWSklPWVFiZ0J2RCUyQjJqeXpzRUN6V3RENEhLSkhuNEd3Z0lmcUVraXZTYkpZeXQ5WE4lMkJCRVlKRHdwUTNtNVFkRHpVU0x2U2tsa0pmUHl6SnEzUUMxcGFGY0lqRldCUkh2OHdsdjl5U01uTWJkSWV5OWRBblB5bEZTQWdoNmhxaGlRYjRlbEk2QzE3Zm5ieHI3cmFONTdqd1ZtYmhuRDdsaUJ3ZTVsUnlCb0FiOXhOem8zd0NaSjVLRjFnVDlyd2VXWUNwR3lnWQ; amp_1a5adb=CLnSJBCbcAUyquCvz0K06G...1hrr2rrmm.1hrr2rvua.1e.5.1j; _ga=GA1.2.2003676706.1710142472; _ga_RSRSMMBH0X=GS1.1.1715327479.6.1.1715328470.38.0.0; tv-repeat-visit=true; tv_user={"authorizationLevel":100,"id":null}; accomSearchbarVariant=control; countryCode=ID; tvl=uEGVAJjpuCxBpknxfQJ3tYKYBpIcosuYgTMEJtSrjhmYL0mreU2YRg1xuFwIaaB2kbEu9PQ9Im2OVPXdfBYZ/3k+weBaf+QWT+Ew2oYjzhoVUFdLWM5vivMGShOYRXOh1654hif6B7mKCz+FBjnAKCTYlE9Th151MU3f/tZ90qltt8dd68rpVfFWIe3r7sS1NzvNYaPErS8sofxYiE4fOYxqRlrUWwmssHgGLb6MqZQPdUVm2TdH+gSr0AuLhSiiB8bQTJ5HhBk=~djAy; tvs=GuleW1s7j7UL4ke9bftYyLbvbtH0+pDnS6JKy0cl86FNTZ2xUM/6Ngv3gFGEi6hM4HozxhKsNLZ6lKfNRSmxd30L6su0aqnAN/XwKJgNA71FP+jUvE+dG3mNRuYRmybfWI6G9tjSH12FOF6hl0WAoVHsF8SCm/93pteiLc7Q+IZ3otjq3W4QWYTO5wxCP8MbP62Qto/H6fMhfJTUR87CHqKPforDk5Hto/ZQUhwLCQk9nomEQYPhvD0deAwtp5cEuU9xatNrSIQkBX1amSTPGNpzp8f78Jq27xU=~djAy; aws-waf-token=8952791e-7b63-4b4a-98ee-f1fde66242ff:GgoAZ7RMR6QXAAAA:EHQKI0HtVlvVO1EKxgO8MDxKomjzgX0z+jZrS61UHX8qIZraJSsyvythjHm8U3jRWukADcqaPFnu0T4si+yUs9cuCdUDnZZqJ7ZkDTtzV8DRkJxVWj2tU7AeArtnsEAyKAbMLceSvzLOKeZvlzL6NYUyGu02XTmnAxCs1bs8iLDlgJOfTuQNjQ+WWe9LAA3A1Ao=; _dd_s=rum=0&expire=1724065822985&logs=1&id=276062d5-3406-41c4-ab14-a66af429d0b0&created=1724064813815')
    # print('cookie: ', cookie_dict)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd('Network.enable', {})
    for cookie in cookie_dict:
        if 'expiry' in cookie:
            cookie['expires'] = cookie['expiry']
            del cookie['expiry']

            # Set the actual cookie
        driver.execute_cdp_cmd('Network.setCookie', cookie)
        
    driver.execute_cdp_cmd('Network.disable', {})
    driver.get('https://www.traveloka.com/en-id/hotel/search?spec=27-09-2024.29-09-2024.2.1.HOTEL_GEO.103570.Surabaya.2')
    
    time.sleep(2)
    no_fetched = 0
    no_failed = 0
    result = {
        'Nama Hotel': [],
        'Rating': [],
        'Lokasi': [],
        'Harga per Malam': [],
    }

    while no_fetched < 200:
        elems_xpath = '/html/body/div[1]/div[5]/div[2]/div/div[2]/div[4]/div/div'
        captcha_xpath = '/html/body/div[28]'
        # /html/body/div[28]/div
        try:
            if driver.find_element(captcha_xpath):
                print('Captcha element found.')
            elems_xpath = '/html/body/div[1]/div[5]/div[2]/div/div[2]/div[3]/div/div'
        except:
            print('Captcha element not found.')
        childs = driver.find_elements(By.XPATH, elems_xpath)
        print('number of elements===>', len(childs), '\nfetched ===>', no_fetched)
        for idx in range(1, 10):
            try:
                child_elem = elems_xpath + f'[{idx+1}]'
                title_xpath = f'{child_elem}/div/div/div/div[2]/div[1]/div[1]/div[1]/h3'
                rating_xpath = f'{child_elem}/div/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]'
                location_xpath = f'{child_elem}/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div/div[2]'
                price_xpath = f'{child_elem}/div/div/div/div[3]/div/div/div[1]/div[3]/div/div[3]/div[1]'

                title = driver.find_element(By.XPATH, title_xpath).text
                rating = driver.find_element(By.XPATH, rating_xpath).text
                location = driver.find_element(By.XPATH, location_xpath).text
                price = driver.find_element(By.XPATH, price_xpath).text
                result['Nama Hotel'].append(title)
                result['Rating'].append(rating)
                result['Lokasi'].append(location)
                result['Harga per Malam'].append(price)

                print(f'{no_fetched}/200 ==> {idx}:\n\tHOTEL {title} - {location} (RATING: {rating})')
                print(f'\tHarga: {price}')

            except Exception as error:
                print(f'{idx} - FAILED: {error}')
                no_failed +=1
            no_fetched += 1

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(5)
    
    try:
        pd.DataFrame(result).to_csv(os.path.join('../results/hasil_scraping.csv'))
        pd.DataFrame(result).to_csv(os.path.join('./hasil_scraping.csv'))
    except:
        pd.DataFrame(result).to_excel(os.path.join('../results/hasil_scraping.csv'))
        pd.DataFrame(result).to_excel(os.path.join('./hasil_scraping.csv'))

    print(f'FAILED: {no_failed}/200')   