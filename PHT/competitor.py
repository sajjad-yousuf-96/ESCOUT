# from ast import keyword
# from click import option
# from selenium import webdriver
from bs4 import BeautifulSoup as bs
# import pandas as pd
import re
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import requests
from bs4 import BeautifulSoup
import json
def main(keyword):
    lst=[]

    url = 'https://www.daraz.pk/catalog/?q='+keyword
    
    # # urlss=request.POST.get("urls")
    # options=Options()
    # options.headless=False
    # options.add_argument('--no-sandbox')         
    # # time.sleep(15)
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
    # # driver = webdriver.Chrome('/home/msy/WORK/NEWESCOUT/ESCOUT/chromedriver',options=options)
    # # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
    # # url="view-source:"+urlss
    # time.sleep(10)
    # driver.switch_to.default_content()

    # driver.get(url)
    # # driver.find_element_by_xpath('//*[@id="q"]').send_keys(keyword)
    # # driver.find_element_by_xpath('//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button').click()
    # page_source = driver.page_source

    # soup = BeautifulSoup(page_source, 'lxml')
    # # soup=BeautifulSoup()
    # # reviews_selector = soup.find_all('div', class_='reviewSelector')

    # productDivs = soup.findAll('div', attrs={'class' : 'box--ujueT'})
    # for div5 in productDivs:
    #     for div4 in div5:
    #         for div3 in div4:
    #             for div2 in div3:
    #                 a=div2.find('a')['href']
    #                 b=re.sub('//', 'https://', a)
    #                 lst.append(b)

    # # for i in lst:
        
    # return lst

# print(main('shampoo'))

    # url = str('https://www.daraz.pk/catalog/?q=')

    # modified-code
    # requesting page to get page source
    response = requests.get(url)
    page_data = BeautifulSoup(response.text,'html.parser')
    # print(page_data)
    last_script_tag = page_data.find_all('script')[-1]
    # print(last_script_tag)
    dict_data = json.loads(last_script_tag.text)
    # print(dict_data)
    main_url = dict_data.get('itemListElement') if dict_data.get('itemListElement') else None
    # print(len(main_url))
    for i in main_url:
        # print(i.get('url'))
        a=i.get('url')
        lst.append(a)
    # print(main_url[2])
    return lst
# main('keychain')