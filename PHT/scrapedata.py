# from webdriver_manager.chrome import ChromeDriverManager
# from .competitor import main
import re
import re
import time
import requests
from bs4 import BeautifulSoup
import json
import sys, os

import datetime
def scrapedata(sku):
    url = str('https://www.daraz.pk/catalog/?q=')
    urls = url + sku
    # modified-code
    # requesting page to get page source
    print(urls)
    response = requests.get(urls)
    page_data = BeautifulSoup(response.text,'html.parser')
    last_script_tag = page_data.find_all('script')[-1]
    # print(last_script_tag)
    dict_data = json.loads(last_script_tag.text)
    # print(dict_data)
    main_url = dict_data.get('itemListElement')[0].get('url') if dict_data.get('itemListElement') else None

    print("Hey niazi: ",main_url)
    try:
    # making main page request
        response_page_source = requests.get(main_url)
        # getting relevant data from page source
        pattern = r"app\.run\((.+)\);"
        page_data = re.search(pattern,response_page_source.text).group(1) if re.search(pattern,response_page_source.text) else None
        main_data = json.loads(page_data)
        
        base_data = main_data.get('data').get('root').get('fields')
        # print(base_data)
        store_discount = base_data.get('skuInfos').get('0').get('price').get('discount')
        original_price = base_data.get('skuInfos').get('0').get('price').get('originalPrice').get('value') if base_data.get('skuInfos').get('0').get('price').get('originalPrice') else base_data.get('skuInfos').get('0').get('price').get('salePrice').get('value')
        print("ITEM-PRICE ",original_price)
        sale_price = base_data.get('skuInfos').get('0').get('price').get('salePrice').get('value')
        stock = base_data.get('skuInfos').get('0').get('stock')
        shopname = base_data.get('seller').get('name')
        print("SHOP-NAME ",shopname)
        ratings = base_data.get('review').get('ratings').get('average')
        
        reviews_data = base_data.get('review').get('ratings').get('reviewTitle')
        review = reviews_data.split(" ")[0] if reviews_data else 0
        print("Review ",review)
        question_answers = base_data.get('qna').get('summaryTitle')
        skud = base_data.get('productOption').get('skuBase').get('skus')[0].get('innerSkuId')
        print("sku ",skud)
        brand = base_data.get('skuInfos').get('0').get('dataLayer').get('brand_name')
        print("Brand ",brand)
        name = base_data.get('skuInfos').get('0').get('dataLayer').get('pdt_name')
        print("RATING ",ratings)
        print("ITEM-NAME ",name)
        
        
        
        
        
        return stock,skud,ratings,name,original_price,shopname,brand,review
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return None

def timestamp():
    times=datetime.datetime.now()
    times=times.strftime("%H:%M:%S")
    da=datetime.date.today()
    # print(times,da)
    return times,da
# timestamp()
# scrapedata('')