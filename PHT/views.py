from django.shortcuts import render,redirect
from django.http import HttpResponse
from selenium import webdriver
from selenium import webdriver
# import scrapy
import re
from selenium import webdriver
import time
# from scrapy.crawler import CrawlerProcess
# from bs4 import BeautifulSoup
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import json

from .forms import *
# from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'PHT/login.html', context)
    
# class daraz(scrapy.Spider):
#     name = "DARAZ"
#     # For headless
#     # option = webdriver.ChromeOptions()
#     # option.add_argument('headless')
    
#     def __init__(self,url,dictt,driver):
#         self.url=url
#         self.dictt=dictt
#         self.driver=driver

#     def start_requests(self):
#         urls=self.url
#         yield scrapy.Request(url=urls,callback=self.parse1)

#     def parse1(self,response):
#         print(response)
#         urls=self.url
#         dictt=self.dictt
#         self.driver.get(response.url)
#         time.sleep(100)
#         # fetchData = response.xpath("//ul[contains(@class,'specification-keys')]//div[contains(@class,'key-value')]/text()").extract()
#         # print("check01: ",fetchData)
#         response=response.replace(body=self.driver.page_source)
#         time.sleep(100)
#         # fetchData = response.xpath("//ul[contains(@class,'specification-keys')]//div[contains(@class,'key-value')]/text()").extract()
#         # print("check02: ",fetchData)

#         # # SKU, brand Name
#         # dictt['SKU'] = fetchData[1]
#         # dictt['brandName'] = fetchData[0]

#         myData = BeautifulSoup(self.driver.page_source,'html.parser')
#         allData = myData.find_all("script")
#         mainData = allData[len(allData)-31]

#         mainData=str(mainData)
#         requiredData = json.loads(mainData[mainData.index("app.run")+8 : mainData.rindex("module_popups")+len("module_popups")+5])
#         dictt['stock'] = requiredData['data']['root']['fields']['skuInfos']['0']['stockList'][0]['stoock']
#         dictt['title'] = requiredData['data']['root']['fields']['product']['title']
#         dictt['avgRating'] = requiredData['data']['root']['fields']['review']['ratings']['average']
#         dictt['totRating'] = requiredData['data']['root']['fields']['review']['ratings']['rateCount']
#         dictt['totReview'] = requiredData['data']['root']['fields']['review']['ratings']['reviewCount']
#         dictt['totQuestions'] = requiredData['data']['root']['fields']['qna']['totalItems']
#         # seller/store name
#         dictt['sellName'] = requiredData['data']['root']['fields']['seller']['name']
#         # chat response rate
#         dictt['respRate'] = requiredData['data']['root']['fields']['seller']['chatResponsiveRate']['value']
#         # sale price / original price
#         if 'originalPrice' in requiredData['data']['root']['fields']['skuInfos']['0']['price']:
#             dictt['orgPrice'] = requiredData['data']['root']['fields']['skuInfos']['0']['price']['originalPrice']['text']
#         dictt['salePrice'] = requiredData['data']['root']['fields']['skuInfos']['0']['price']['salePrice']['text']

#         print("total is",dictt)
        
def register(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/") 
    context={'form':form}
    return render(request,'PHT/register.html',context)
def logoutP(request):
	logout(request)
	return redirect('index')

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    if request.method=="POST" and request.POST.get('URLS')=='URLS':
        print(request.POST.dict())
        # new=request.POST.dict()
        # new=list(new.items())
        # print(list(new))
        urlss=request.POST.get("urls")
        options=Options()
        options.headless=True
        # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
        driver = webdriver.Chrome('/home/msy/WORK/NEWESCOUT/ESCOUT/chromedriver',chrome_options=options)
        # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
        # url="view-source:"+urlss
        driver.get(urlss)
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
        a=re.findall("ratings.:..average.:...",read)
        ratings=a[0][20::]
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
        userid=request.user.id
        obj=UserScrapeData.objects.create(userid=userid,sku=skud,stock=stock,ratings=ratings,item_name=name,shop_name=shopname,item_price=price,brand=brand,review=review)
        obj.save()
        product=UserScrapeData.objects.last()
        try:
            print(product.id)
            red="/product/"+str(product.id)
            return redirect(red)
        except Exception as error:
            return render(request,"PHT/dashboard.html")
    elif request.method=="POST" and request.POST.get('URLS')=='SKU':
        url = str('https://www.daraz.pk/catalog/?q=')
        skus=request.POST.get('urls')
        urlss=url+skus
        options=Options()
        options.headless=True
        # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
        driver = webdriver.Chrome('/home/msy/WORK/NEWESCOUT/ESCOUT/chromedriver',chrome_options=options)
        # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
        # url="view-source:"+urlss
        driver.get(urlss)
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
        a=re.findall("ratings.:..average.:...",read)
        ratings=a[0][20::]
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
        userid=request.user.id
        obj=UserScrapeData.objects.create(userid=userid,sku=skud,stock=stock,ratings=ratings,item_name=name,shop_name=shopname,item_price=price,brand=brand,review=review)
        obj.save()
        product=UserScrapeData.objects.last()
        try:
            print(product.id)
            red="/product/"+str(product.id)
            return redirect(red)
        except Exception as error:
            return render(request,"PHT/dashboard.html")


    # if request.method=="POST":
        
        


    #     dictt={}
    #     driver = webdriver.Chrome("E:/DJ/niazi/chromedriver.exe")
    #     radio=1
    #     # user based selection
    #     # sel = int(input("Please select: \n1. SKU\n2. URL"))
    #     if radio == 1:
    #         driver.get("https://www.daraz.pk/#")
    #         user='220294946_PK-1433739908'
    #         time.sleep(5)
    #         driver.find_element_by_id("q").send_keys(user)
    #         driver.find_element_by_xpath("//div[@class='search-box__search--2fC5']/button[@class='search-box__button--1oH7']").click()
    #         # element = driver.find_element_by_xpath("//div[@class='search-box__search--2fC5']/button[@class='search-box__button--1oH7']")
    #         # driver.execute_script("arguments[0].click();", element)
    #         time.sleep(5)
    #         driver.find_element_by_xpath("//div[@class='c1_t2i']/div[@class='c2prKC']//a[1]").click()
    #         time.sleep(20)
    #         urll=driver.current_url
    #         print(urll)
    #     else:
    #         urll=input("Please Enter the URL: ")
    #     process = CrawlerProcess()
    #     process.crawl(daraz,urll,dictt,driver)
    #     process.start()

    userid=request.user.id
    datas=UserScrapeData.objects.filter(userid=userid)  
    print(datas)
    context={'datas':datas}
    return render(request,"PHT/dashboard.html",context)
    

#####################################
        
                



        


########################################

@login_required(login_url='login')
def profitcalculator(request):
    if request.method=="POST":
        new=request.POST.dict()
        lst=list(new.items())
        phf=float(lst[7][1])
        vat=int(lst[6][1])
        selling_price=int(lst[2][1])
        cat=request.POST.get("category")
        cate=CommissionList.objects.get(category=cat)
        # print(cate.commissions)
        category=cate.commissions
        category=category.strip("%")
        category=float(category)
        # print(type(category))
        dc=selling_price*(category/100) ### DARAZ COMMISSION
        print("daraz COMMISSION fee",dc)
        paymentfee=(selling_price*phf)/100 #payment handling fee 1.25% of sell Price
        print("PAY handling fee",paymentfee)
        vats=int(lst[3][1])*vat/100
        vatf=dc+paymentfee*vat/100
        print("VAT on Daraz Commission and Payment Fee (16%)",vatf)
        print("VAT on Shipping FEE (16%)",vats)
        daraz_comm_total=dc+paymentfee+vatf+vat+10
        print("Sub Total Daraz Expenses/ Commissions ",daraz_comm_total)
        total_expense=daraz_comm_total+int(lst[4][1])
        print("TOTAL EXPENSES (Sourcing Cost + Daraz Fees)",total_expense)
        net_profit=(selling_price-total_expense)
        print("Net Profit (Per Product/ Unit) ",net_profit)
        monthprofi=round(net_profit*int(lst[5][1]))
        Revenue=selling_price*int(lst[5][1])
        print("Total Expected profit in a Month",monthprofi)
        cate=CommissionList.objects.all()


        context={'cate':cate,'Commission':category,'PHF':phf,'VAT':vat,'VATS':vats,
                'VATF':vatf,'DE':daraz_comm_total,'TOTAL':total_expense,
                'selling_price':selling_price,'PROFIT':net_profit,
                'Revenue':Revenue,'PROFITM':monthprofi}
        return render(request,"PHT/profit.html",context)
    else:    
        cate=CommissionList.objects.all()
        print(cate)
        context={'cate':cate}
        return render(request,"PHT/profit.html",context)

def index(request):
    return render(request,'PHT/index.html')
@login_required(login_url='login')
def product(request,pk):
    # print(request.user.id)
    # userid=request.user.id
    # pid=pk
    product=UserScrapeData.objects.get(id=pk)
    print(product)
    context={'product':product}
    return render(request,'PHT/product.html',context)  

def databasePage(request):
    print("database")
    return render(request,'PHT/database.html')      