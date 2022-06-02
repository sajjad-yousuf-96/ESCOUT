from pydoc import text
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from selenium import webdriver
from selenium import webdriver
from django.db.models import Q
import datetime
# import scrapy
from webdriver_manager.chrome import ChromeDriverManager
from .competitor import main
from .scrapedata import scrapedata,timestamp
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
        driver = webdriver.Chrome(ChromeDriverManager().install())
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
        userid=request.user.id
        t=timestamp()
        print(t)
        # times=datetime.datetime.now()
        # times=times.strftime("%H:%M:%S")
        # dates=datetime.date.today()
        # print(times)
        # print(dates)
        obj=UserScrapeData.objects.create(userid=userid,sku=skud,stock=stock,ratings=ratings,item_name=name,shop_name=shopname,item_price=price,brand=brand,review=review,time=t[0],date=t[1])
        obj.save()
        # product=UserScrapeData.objects.last()
        # try:
        #     print(product.id)
        #     red="/product/"+str(product.id)
        #     return redirect(red)
        # except Exception as error:
        #     return render(request,"PHT/dashboard.html")
    elif request.method=="POST" and request.POST.get('URLS')=='SKU':
        url = str('https://www.daraz.pk/catalog/?q=')
        skus=request.POST.get('urls')
        urlss=url+skus
        options=Options()
        options.headless=True
        # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
        driver = webdriver.Chrome(ChromeDriverManager().install())
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
        userid=request.user.id
        t=timestamp()

        # times=datetime.datetime.now()
        # times=times.strftime("%H:%M:%S")
        # dates=datetime.date.today()
        # print(times)
        # print(dates)
        obj=UserScrapeData.objects.create(userid=userid,sku=skud,stock=stock,ratings=ratings,item_name=name,shop_name=shopname,item_price=price,brand=brand,review=review,time=t[0],date=t[1])
        obj.save()
        # product=UserScrapeData.objects.last()
        # try:
        #     # print(product.id)
        #     red="/product/"+str(product.id)
        #     return redirect(red)
        # except Exception as error:
        #     return render(request,"PHT/dashboard.html")


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
    if request.method == 'POST' and request.POST.get('Schedular'):
        print(request.POST)
        print(pk)
        pk_id=pk
        seconds=request.POST.get('seconds')
        seconds=int(seconds)
        print(type(seconds))
        print(request.user.id)
        userid=request.user.id
        data=UserScrapeData.objects.get(id=pk)
        # times=datetime.datetime.now()
        # times=times.strftime("%H:%M:%S")
        # dates=datetime.date.today()
        print("s",data)
        obj=UserProductsTracking.objects.create(userid=userid,sku=data.sku,stock=data.stock,ratings=data.ratings,item_name=data.item_name,shop_name=data.shop_name,item_price=data.item_price,brand=data.brand,review=data.review,time=data.time,date=data.date,product_id=pk_id)
        obj.save()
        print("WAit",seconds,"Seconds")
        time.sleep(seconds)
        d=scrapedata(data.sku)
        print(d[1])
        times=datetime.datetime.now()
        times=times.strftime("%H:%M:%S")
        dates=datetime.date.today()
        obj=UserProductsTracking.objects.create(userid=userid,sku=d[1],stock=d[0],ratings=d[2],item_name=d[3],shop_name=d[5],item_price=d[4],brand=d[6],review=d[7],time=times,date=dates,product_id=pk_id)
        obj.save()
    elif request.method == 'POST' and request.POST.get('Profit'):
        print(request.POST)
        print(pk)
        data=UserScrapeData.objects.get(id=pk)
        print(data)
        price=data.item_price
        price=price.replace("Rs. ","")
        try:
            price=price.replace(",","")
            price=int(price)
            sourcing=int(price/4)
            cate=CommissionList.objects.all()
            # print(cate)
            # context={'cate':cate}
            # return render(request,"PHT/profit.html",context)
            context={'price':price,'sourcing':sourcing,'cate':cate}
            return render(request,'PHT/productcalculator.html',context) 
        except:
            price=int(price)
            sourcing=int(price/4)
            cate=CommissionList.objects.all()
            # print(cate)
            # context={'cate':cate}
            # return render(request,"PHT/profit.html",context)
            context={'price':price,'sourcing':sourcing,'cate':cate}
            return render(request,'PHT/productcalculator.html',context) 
    userid=request.user.id
    pid=pk
    products=UserScrapeData.objects.get(id=pk)
    # print(products.sku)
    # skus=products.sku
    if UserProductsTracking.objects.filter(Q(sku=products.sku) & Q(product_id=products.id)):
        products=UserProductsTracking.objects.filter(Q(sku=products.sku) & Q(product_id=products.id))
        print("sa",products)
        context={'products':products}
        return render(request,'PHT/product.html',context)
    else:
        products=UserScrapeData.objects.filter(id=pk)
        print("s",products) 
        context={'products':products}
        return render(request,'PHT/product.html',context) 
    # try:
    #     products=UserProductsTracking.objects.filter(Q(sku=products.sku) & Q(product_id=products.id))
    #     print("sa",products)
    #     context={'products':products}
    #     return render(request,'PHT/product.html',context)
    # except:
    #     products=UserScrapeData.objects.filter(id=pk)
    #     print("s",products.sku) 
    #     context={'products':products}
    # return render(request,'PHT/product.html')  

def databasePage(request):
    # products=CommissionList.objects.all()
    products= CategoryRecords.objects.all()
    print(products)
    context={'products':products}
    return render(request,'PHT/database.html',context)


@login_required(login_url='login')
def darazCommission(request):
    allData = CommissionList.objects.all()
    if(request.method=="POST"):
        keyword=request.POST.get('category')
        allData=CommissionList.objects.filter(category__icontains=keyword) 
    return render(request,'PHT/commissionPage.html',{'allData' : allData})

def datacompetitor(request):
    if request.method=="POST":
        print(request.POST)
        keyword=request.POST.get('Keyword')
        how=request.POST.get('howmany')
        how=int(how)
        data=main(keyword)
        # print(data)
        data=data[0:how]
        print(data)
        userid=request.user.id
        
        try:
            for urls in data:
                options=Options()
                options.headless=False
                # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
                driver = webdriver.Chrome(ChromeDriverManager().install())
                print(urls)
                # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
                # url="view-source:"+urlss
                driver.get(urls)
                time.sleep(15)
                # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div').click()
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
                obj=CompetitorData.objects.create(search_name=keyword,userid=userid,product_url=urls,product_title=name,item_price=price,review=review,product_sku=skud,stock=stock,ratings=ratings)
                obj.save()
            
        except Exception as error:
            print(error)
    userid=request.user.id
    datas=CompetitorData.objects.filter(userid=userid).order_by('search_name')  
    # print(datas)
    cate=CompetitorData.objects.filter(userid=userid)
    keywordlst=[]
    for i in cate:
        if i.search_name not in keywordlst:
            keywordlst.append(i.search_name)
    
    # context={'cate':cate}
    # return render(request,"PHT/profit.html",context)
    context={'datas':datas,"keywordlst":keywordlst}
    return render(request,'PHT/competitorpage.html',context)

def productcalculator(request):
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
        return render(request,"PHT/productcalculator.html",context)


def keywordtracking(request):
    if request.method=="POST":
        userid=request.user.id
        print(request.POST)
        keyword=request.POST['keyword']
        select_sku=CompetitorData.objects.filter(Q(userid=userid) & Q(search_name=keyword))
        for i in select_sku:
            url = str('https://www.daraz.pk/catalog/?q=')
            urlss=url+i.product_sku
            options=Options()
            options.headless=True
            # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
            driver = webdriver.Chrome(ChromeDriverManager().install())
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
            urls=driver.current_url
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
            # print(stock)
            userid=request.user.id
            obj=CompetitorData.objects.create(search_name=keyword,userid=userid,product_url=urls,product_title=name,item_price=price,review=review,product_sku=skud,stock=stock,ratings=ratings)
            obj.save()


        return redirect("datacompetitor")
