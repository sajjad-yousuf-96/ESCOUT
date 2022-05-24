from ast import keyword
from click import option
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def main(keyword):
    lst=[]

    url = 'https://www.daraz.pk/catalog/?q='+keyword
    
    # urlss=request.POST.get("urls")
    options=Options()
    options.headless=False
    options.add_argument('--no-sandbox')         
    # time.sleep(15)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
    # driver = webdriver.Chrome('/home/msy/WORK/NEWESCOUT/ESCOUT/chromedriver',options=options)
    # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
    # url="view-source:"+urlss
    time.sleep(10)
    driver.switch_to.default_content()

    driver.get(url)
    # driver.find_element_by_xpath('//*[@id="q"]').send_keys(keyword)
    # driver.find_element_by_xpath('//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button').click()
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    # soup=BeautifulSoup()
    # reviews_selector = soup.find_all('div', class_='reviewSelector')

    productDivs = soup.findAll('div', attrs={'class' : 'box--ujueT'})
    for div5 in productDivs:
        for div4 in div5:
            for div3 in div4:
                for div2 in div3:
                    a=div2.find('a')['href']
                    b=re.sub('//', 'https://', a)
                    lst.append(b)

    # for i in lst:
        
    return lst

# print(main('shampoo'))