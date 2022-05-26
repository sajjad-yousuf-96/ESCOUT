from webdriver_manager.chrome import ChromeDriverManager
# from .competitor import main
import re
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import datetime
def scrapedata(sku):
    url = str('https://www.daraz.pk/catalog/?q=')
    urls=url+sku
    options=Options()
    options.headless=False
    # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
    # url="view-source:"+urlss
    driver.get(urls)
    time.sleep(15)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div').click()
    driver.execute_script("window.scrollTo(0, 1350)")
    driver.execute_script("window.scrollTo(0, 1250)")
    driver.execute_script("window.scrollTo(0, 1150)")
    driver.execute_script("window.scrollTo(0, 1050)")
    driver.execute_script("window.scrollTo(0, 1050)")
    time.sleep(20)
    driver.execute_script("window.scrollTo(0, 1150)")
    driver.execute_script("window.scrollTo(0, 1250)")
    # a=driver.find_element_by_xpath('/html/body/div[4]/div/div[8]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
    p = driver.page_source
    name=driver.find_element_by_xpath('//*[@id="module_product_title_1"]/div/div/span').text
    price=driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/span').text
    shopname=driver.find_element_by_xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a').text
    review=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
    
    brand=driver.find_element_by_xpath('//*[@id="module_product_brand_1"]/div/a[1]').text
    review=review.split(" ")
    review=review[0]
    
    read=str(p) #Needed to do as the file encoding is undefined
    # cap=""
    # a=re.findall("ratings.:..average.:...",read)
    ratings=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[3]').text
    print(ratings)
    skudata=re.findall("SKU.:........................",read)
    # stockdata=re.findall("stoock.:....",read)
    for i in skudata:
        skud=i[6::]
        print("SKU ",skud)
        break
    p=re.compile(r'"stoock":(\w+)')
    m=p.finditer(read)
    for i in m:
        stock=i.group(1)
        print(i.group(1))
        break
    print("RATING ",ratings)
    print("ITEM-NAME ",name)
    print("ITEM-PRICE ",price)
    print("SHOP-NAME ",shopname)
    print("Review ",review)
    print("Brand ",brand)
    return stock,skud,ratings,name,price,shopname,brand,review

def timestamp():
    times=datetime.datetime.now()
    times=times.strftime("%H:%M:%S")
    da=datetime.date.today()
    print(times,da)
    return times,da
timestamp()