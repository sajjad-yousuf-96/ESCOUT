# from webdriver_manager.chrome import ChromeDriverManager
# from .competitor import main
import re
import time
import requests
from bs4 import BeautifulSoup
import json

def scrapedata(sku):
    url = str('https://www.daraz.pk/catalog/?q=')
    urls = url + sku
    # modified-code
    # requesting page to get page source
    response = requests.get(urls)
    page_data = BeautifulSoup(response.text,'html.parser')
    last_script_tag = page_data.find_all('script')[-1]
    # print(last_script_tag)
    dict_data = json.loads(last_script_tag.text)
    main_url = dict_data.get('itemListElement')[0].get('url') if dict_data.get('itemListElement') else None

    # print("Hey niazi: ",main_url)

    # making main page request
    response_page_source = requests.get(main_url)
    # getting relevant data from page source
    pattern = r"app\.run\((.+)\);"
    page_data = re.search(pattern,response_page_source.text).group(1) if re.search(pattern,response_page_source.text) else None
    main_data = json.loads(page_data)
    base_data = main_data.get('data').get('root').get('fields')
    
    store_discount = base_data.get('skuInfos').get('0').get('price').get('discount')
    original_price = base_data.get('skuInfos').get('0').get('price').get('originalPrice').get('value')
    sale_price = base_data.get('skuInfos').get('0').get('price').get('salePrice').get('value')
    stock = base_data.get('skuInfos').get('0').get('stock')
    seller_name = base_data.get('seller').get('name')
    avg_ratings = base_data.get('review').get('ratings').get('average')
    
    reviews_data = base_data.get('review').get('ratings').get('reviewTitle')
    reviews = reviews_data.split(" ")[0] if reviews_data else 0
    
    question_answers = base_data.get('qna').get('summaryTitle')
    sku_id = base_data.get('productOption').get('skuBase').get('skus')[0].get('innerSkuId')
    brand_name = base_data.get('skuInfos').get('0').get('dataLayer').get('brand_name')
    product_name = base_data.get('skuInfos').get('0').get('dataLayer').get('pdt_name')
    # seller_name = base_data.get('skuInfos').get('0').get('dataLayer').get('seller_name')


    print("HEY NIAZI: ",store_discount," ",original_price," ",sale_price," ",stock," ",seller_name," ",avg_ratings," ",reviews," ",question_answers," ",sku_id," ",brand_name," ",product_name," ",seller_name)

# initial_time = time.time()
scrapedata('112178807_PK-1263650772')
# print("TOTAL TIME TAKEN FOR 1 SKU: ",time.time() - initial_time)

