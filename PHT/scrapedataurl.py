from webdriver_manager.chrome import ChromeDriverManager
# from .competitor import main
import re
import re
import time
import requests
from bs4 import BeautifulSoup
import json

import datetime
def scrapedataurl(urls):
    # url = str('https://www.daraz.pk/catalog/?q=')
    # urls = url + sku
    # modified-code
    # requesting page to get page source
    print(urls)
    # response = requests.get(urls)
    # page_data = BeautifulSoup(response.text,'html.parser')
    # # print(page_data)
    # last_script_tag = page_data.find_all('script')[-1]

    # print(last_script_tag)
    # dict_data = json.loads(last_script_tag.text)
    # main_url = dict_data.get('itemListElement')[0].get('url') if dict_data.get('itemListElement') else None

    # print("Hey niazi: ",main_url)

    # making main page request
    response_page_source = requests.get(urls)
    # getting relevant data from page source
    pattern = r"app\.run\((.+)\);"
    page_data = re.search(pattern,response_page_source.text).group(1) if re.search(pattern,response_page_source.text) else None
    main_data = json.loads(page_data)
    base_data = main_data.get('data').get('root').get('fields')
    
    store_discount = base_data.get('skuInfos').get('0').get('price').get('discount')
    price = base_data.get('skuInfos').get('0').get('price').get('originalPrice').get('value')
    sale_price = base_data.get('skuInfos').get('0').get('price').get('salePrice').get('value')
    stock = base_data.get('skuInfos').get('0').get('stock')
    shopname = base_data.get('seller').get('name')
    ratings = base_data.get('review').get('ratings').get('average')
    
    reviews_data = base_data.get('review').get('ratings').get('reviewTitle')
    review = reviews_data.split(" ")[0] if reviews_data else 0
    
    question_answers = base_data.get('qna').get('summaryTitle')
    skud = base_data.get('productOption').get('skuBase').get('skus')[0].get('innerSkuId')
    brand = base_data.get('skuInfos').get('0').get('dataLayer').get('brand_name')
    name = base_data.get('skuInfos').get('0').get('dataLayer').get('pdt_name')
    print("RATING ",ratings)
    print("ITEM-NAME ",name)
    print("ITEM-PRICE ",price)
    print("SHOP-NAME ",shopname)
    print("Review ",review)
    print("Brand ",brand)
    print("Brand ",skud)
    return stock,skud,ratings,name,price,shopname,brand,review

def timestamp():
    times=datetime.datetime.now()
    times=times.strftime("%H:%M:%S")
    da=datetime.date.today()
    # print(times,da)
    return times,da
# timestamp()