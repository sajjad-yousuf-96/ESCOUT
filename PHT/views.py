from pydoc import text
from django import urls
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
# from selenium import webdriver
# from selenium import webdriver
import pandas as pd
from django.db.models import Q
import datetime
import os
import pandas as pd
from random import randint
from tkinter.filedialog import asksaveasfile
import csv
from .scrapedataurl import scrapedataurl
# import scrapy
# from webdriver_manager.chrome import ChromeDriverManager
from .competitor import main
from .scrapedata import scrapedata,timestamp
import re
# from selenium import webdriver
import time
# from scrapy.crawler import CrawlerProcess
# from bs4 import BeautifulSoup
import json
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
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
    # print(request.POST)
    if request.method=='POST':

        if request.method=="POST" and request.POST.get('URLS')=='URLS':
            try:
                print(request.POST.dict())
                start = time.time()
                # new=request.POST.dict()
                # new=list(new.items())
                # print(list(new))
                urlss=request.POST.get("urls")
                data=scrapedataurl(urlss)
                # options=Options()
                # options.headless=True
                # # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
                # driver = webdriver.Chrome(ChromeDriverManager().install())
                # # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
                # # url="view-source:"+urlss
                # driver.get(urlss)
                # driver.maximize_window()
                # driver.execute_script("window.scrollTo(0, 1350)")
                # driver.execute_script("window.scrollTo(0, 1250)")
                # driver.execute_script("window.scrollTo(0, 1150)")
                # driver.execute_script("window.scrollTo(0, 1050)")
                # driver.execute_script("window.scrollTo(0, 1050)")
                # time.sleep(20)
                # driver.execute_script("window.scrollTo(0, 1150)")
                # driver.execute_script("window.scrollTo(0, 1250)")
                # # a=driver.find_element_by_xpath('/html/body/div[4]/div/div[8]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
                # p = driver.page_source
                # name=driver.find_element_by_xpath('//*[@id="module_product_title_1"]/div/div/span').text
                # price=driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/span').text
                # shopname=driver.find_element_by_xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a').text
                # review=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
                
                # brand=driver.find_element_by_xpath('//*[@id="module_product_brand_1"]/div/a[1]').text
                # review=review.split(" ")
                # review=review[0]
                # read=str(p) #Needed to do as the file encoding is undefined
                # # cap=""
                # a=re.findall("ratings.:..average.:...",read)
                # ratings=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[3]').text
                # print(ratings)
                # skudata=re.findall("SKU.:........................",read)
                # # stockdata=re.findall("stoock.:....",read)
                # for i in skudata:
                #     skud=i[6::]
                #     print("SKU ",skud)
                #     break
                # p=re.compile(r'"stoock":(\w+)')
                # m=p.finditer(read)
                # for i in m:
                #     stock=i.group(1)
                #     print(i.group(1))
                #     break
                # print("RATING ",ratings)
                # print("ITEM-NAME ",name)
                # print("ITEM-PRICE ",price)
                # print("SHOP-NAME ",shopname)
                # print("Review ",review)
                # print("Brand ",brand)
                userid=request.user.id
                t=timestamp()
                print(t)
                print(data)
                # times=datetime.datetime.now()
                # times=times.strftime("%H:%M:%S")
                # dates=datetime.date.today()
                # print(times)
                # print(dates)
                obj=UserScrapeData.objects.create(userid=userid,sku=data[1],stock=data[0],ratings=data[2],item_name=data[3],shop_name=data[5],item_price=data[4],brand=data[6],review=data[7],time=t[0],date=t[1])
                obj.save()
                end = time.time()
                print(end-start,"seconds")
                # product=UserScrapeData.objects.last()
                # try:
                #     print(product.id)
                #     red="/product/"+str(product.id)
                #     return redirect(red)
                # except Exception as error:
                #     return render(request,"PHT/dashboard.html")
            except:
                messages.info(request, 'Incorrect URL or SKU/ FIRST SELECT ANY OPTION URL OR SKU')

        elif request.method=="POST" and request.POST.get('URLS')=='SKU':
            try:
                # url = str('https://www.daraz.pk/catalog/?q=')
                skus=request.POST.get('urls')
                # urlss=url+skus
                data=scrapedata(skus)
                # options=Options()
                # options.headless=True
                # # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
                # driver = webdriver.Chrome(ChromeDriverManager().install())
                # # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
                # # url="view-source:"+urlss
                # driver.get(urlss)
                # time.sleep(15)
                # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div').click()
                # driver.maximize_window()
                # driver.execute_script("window.scrollTo(0, 1350)")
                # driver.execute_script("window.scrollTo(0, 1250)")
                # driver.execute_script("window.scrollTo(0, 1150)")
                # driver.execute_script("window.scrollTo(0, 1050)")
                # driver.execute_script("window.scrollTo(0, 1050)")
                # time.sleep(20)
                # driver.execute_script("window.scrollTo(0, 1150)")
                # driver.execute_script("window.scrollTo(0, 1250)")
                # # a=driver.find_element_by_xpath('/html/body/div[4]/div/div[8]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
                # p = driver.page_source
                # name=driver.find_element_by_xpath('//*[@id="module_product_title_1"]/div/div/span').text
                # price=driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/span').text
                # shopname=driver.find_element_by_xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a').text
                # review=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
                
                # brand=driver.find_element_by_xpath('//*[@id="module_product_brand_1"]/div/a[1]').text
                # review=review.split(" ")
                # review=review[0]
                
                # read=str(p) #Needed to do as the file encoding is undefined
                # # cap=""
                # # a=re.findall("ratings.:..average.:...",read)
                # ratings=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[3]').text
                # print(ratings)
                # skudata=re.findall("SKU.:........................",read)
                # # stockdata=re.findall("stoock.:....",read)
                # for i in skudata:
                #     skud=i[6::]
                #     print("SKU ",skud)
                #     break
                # p=re.compile(r'"stoock":(\w+)')
                # m=p.finditer(read)
                # for i in m:
                #     stock=i.group(1)
                #     print(i.group(1))
                #     break
                # print("RATING ",ratings)
                # print("ITEM-NAME ",name)
                # print("ITEM-PRICE ",price)
                # print("SHOP-NAME ",shopname)
                # print("Review ",review)
                # print("Brand ",brand)
                userid=request.user.id
                t=timestamp()
                print(data)
                # times=datetime.datetime.now()
                # times=times.strftime("%H:%M:%S")
                # dates=datetime.date.today()
                # print(times)
                # print(dates)
                obj=UserScrapeData.objects.create(userid=userid,sku=data[1],stock=data[0],ratings=data[2],item_name=data[3],shop_name=data[5],item_price=data[4],brand=data[6],review=data[7],time=t[0],date=t[1])
                obj.save()
            except:
                messages.info(request, 'Incorrect URL or SKU/ FIRST SELECT ANY OPTION URL OR SKU')

        # product=UserScrapeData.objects.last()
        # try:
        else:
            print("ERR")
            messages.info(request, 'Incorrect URL or SKU/ FIRST SELECT ANY OPTION URL OR SKU')
    
    userid=request.user.id
    datas=UserScrapeData.objects.filter(userid=userid)  
    print(datas)
    if datas.exists():
        avgpricelst=[]
        for i in datas:
            a=i.item_price
            a=a.replace('Rs. ','')
            if a.replace(',',''):
                a=a.replace(',','')
            # print(a.isdigit())
            avgpricelst.append(int(a))
        avgpricelst=sum(avgpricelst)/len(avgpricelst)

        avgreviewlst=[]
        for i in datas:
            a=i.review
            # print(a)
            if a.replace('/5',''):
                a=a.replace('/5','')
            # print(a)
            avgreviewlst.append(float(a))
        avgreviewlst=sum(avgreviewlst)/len(avgreviewlst)
        avgreviewlst=round(avgreviewlst)
        # print(avgreviewlst)
        avgratinglst=[]
        for i in datas:
            a=i.ratings
            if a.replace(' Ratings',''):
                a=a.replace(' Ratings','')
            # print(a.isdigit())
            avgratinglst.append(float(a))
        avgratinglst=sum(avgratinglst)/len(avgratinglst)
        avgratinglst=round(avgratinglst)
        context={'datas':datas,'avgpricelst':avgpricelst,'avgreviewlst':avgreviewlst,'avgratinglst':avgratinglst}
        return render(request,"PHT/dashboard.html",context)
    else:
        context={}
        return render(request,"PHT/dashboard.html",context)

########################################
@login_required(login_url='login')
def exporttocsv(request):
    # print(request.POST)
    if 'exportcsv' in request.POST:
        def save():
            files = [('Comma Separated Files', '*.csv')]
            file = asksaveasfile(filetypes = files, defaultextension = files)
            return file
        a=save()
        # print(type(a.name))
        filename=a.name
        # print(a.get('name'))
        userid=request.user.id

        datas=UserScrapeData.objects.filter(userid=userid)
        
        arr = []
        header=['sku','stock','ratings','item_name','shop_name','item_price','brand','review','time','date']

        for i in datas:
            newlst=[]
            newlst.append(i.sku)
            newlst.append(i.stock)
            newlst.append(i.ratings)
            newlst.append(i.item_name)
            newlst.append(i.shop_name)
            newlst.append(i.item_price)
            newlst.append(i.brand)
            newlst.append(i.review)
            newlst.append(i.time)
            newlst.append(i.date)
            arr.append(newlst)
        # print(arr)
            # break

        with open(filename,'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(arr)
        print("csv")
        return redirect("dashboard")
    elif 'refresh' in request.POST:
        userid=request.user.id
        datas=UserScrapeData.objects.filter(userid=userid)
        if datas.exists():
            for i in datas:
                d=scrapedata(i.sku)
                obj=UserProductsTracking.objects.filter(product_id=i.id)
                print(obj)
                if obj.exists():
                    # print("s",data)
                    print('if')
                    # obj=UserProductsTracking.objects.create(userid=userid,sku=data.sku,stock=data.stock,ratings=data.ratings,item_name=data.item_name,shop_name=data.shop_name,item_price=data.item_price,brand=data.brand,review=data.review,time=data.time,date=data.date,product_id=pk_id)
                    # obj.save()
                    # print("WAit",seconds,"Seconds")
                    # time.sleep(seconds)
                    print(d[1])
                    times=datetime.datetime.now()
                    times=times.strftime("%H:%M:%S")
                    dates=datetime.date.today()
                    obj=UserProductsTracking.objects.create(userid=userid,sku=d[1],stock=d[0],ratings=d[2],item_name=d[3],shop_name=d[5],item_price=d[4],brand=d[6],review=d[7],time=times,date=dates,product_id=i.id)
                    obj.save()
                elif d:
                    # print("s",data)
                    print('elif')
                    obj=UserProductsTracking.objects.create(userid=userid,sku=datas.sku,stock=datas.stock,ratings=datas.ratings,item_name=datas.item_name,shop_name=datas.shop_name,item_price=datas.item_price,brand=datas.brand,review=datas.review,time=datas.time,date=datas.date,product_id=i.id)
                    obj.save()
                    # print("WAit",seconds,"Seconds")
                    # time.sleep(seconds)
                    print(d[1])
                    times=datetime.datetime.now()
                    times=times.strftime("%H:%M:%S")
                    dates=datetime.date.today()
                    obj=UserProductsTracking.objects.create(userid=userid,sku=d[1],stock=d[0],ratings=d[2],item_name=d[3],shop_name=d[5],item_price=d[4],brand=d[6],review=d[7],time=times,date=dates,product_id=i.id)
                    obj.save()
                else:
                    pass
            return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        user=request.user.id
        # print(request.POST)
        print(request.FILES['SAJJAD'])
        a=request.FILES['SAJJAD']
        new=CsvSaveFile.objects.create(userid=user,csvfile=a)
        new.save()
        s=CsvSaveFile.objects.last()
        # print(s.file.path)
        paths=s.csvfile.path
        print(paths)
        userid=request.user.id
        df = pd.read_csv(paths)
        country = df['sku']
        for x in country:
            data=scrapedata(str(x))
            if data:
                
                t=timestamp()
                print(data)
                # times=datetime.datetime.now()
                # times=times.strftime("%H:%M:%S")
                # dates=datetime.date.today()
                # print(times)
                # print(dates)
                obj=UserScrapeData.objects.create(userid=userid,sku=data[1],stock=data[0],ratings=data[2],item_name=data[3],shop_name=data[5],item_price=data[4],brand=data[6],review=data[7],time=t[0],date=t[1])
                obj.save()
        return redirect("dashboard")
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
        namelst=['total_expense','selling_price','net_profit','Revenue','monthprofi']
        graphlst=[total_expense,selling_price,net_profit,Revenue,monthprofi]
        print(graphlst)
        color = []
        n = len(graphlst)

        for i in range(n):
            color.append('#%06X' % randint(0, 0xFFFFFF))
        print(color)

        context={'cate':cate,'Commission':category,'PHF':phf,'VAT':vat,'VATS':vats,
                'VATF':vatf,'DE':daraz_comm_total,'TOTAL':total_expense,
                'selling_price':selling_price,'PROFIT':net_profit,
                'Revenue':Revenue,'PROFITM':monthprofi,'graphlst':graphlst,'color':color,'namelst':namelst}

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
        # print(pk)
        pk_id=pk
        seconds=request.POST.get('seconds')
        seconds=int(seconds)
        # print(type(seconds))
        # print(request.user.id)
        userid=request.user.id
        data=UserScrapeData.objects.get(id=pk)
        # times=datetime.datetime.now()
        # times=times.strftime("%H:%M:%S")
        # dates=datetime.date.today()
        print(data.sku)
        try:
            d=scrapedata(data.sku)
            obj=UserProductsTracking.objects.filter(product_id=data.id)
            print(obj)
            if obj.exists():
                # print("s",data)
                print('if')
                # obj=UserProductsTracking.objects.create(userid=userid,sku=data.sku,stock=data.stock,ratings=data.ratings,item_name=data.item_name,shop_name=data.shop_name,item_price=data.item_price,brand=data.brand,review=data.review,time=data.time,date=data.date,product_id=pk_id)
                # obj.save()
                print("WAit",seconds,"Seconds")
                time.sleep(seconds)
                print(d[1])
                times=datetime.datetime.now()
                times=times.strftime("%H:%M:%S")
                dates=datetime.date.today()
                obj=UserProductsTracking.objects.create(userid=userid,sku=d[1],stock=d[0],ratings=d[2],item_name=d[3],shop_name=d[5],item_price=d[4],brand=d[6],review=d[7],time=times,date=dates,product_id=pk_id)
                obj.save()
            elif d:
                # print("s",data)
                print('elif')
                obj=UserProductsTracking.objects.create(userid=userid,sku=data.sku,stock=data.stock,ratings=data.ratings,item_name=data.item_name,shop_name=data.shop_name,item_price=data.item_price,brand=data.brand,review=data.review,time=data.time,date=data.date,product_id=pk_id)
                obj.save()
                print("WAit",seconds,"Seconds")
                time.sleep(seconds)
                print(d[1])
                times=datetime.datetime.now()
                times=times.strftime("%H:%M:%S")
                dates=datetime.date.today()
                obj=UserProductsTracking.objects.create(userid=userid,sku=d[1],stock=d[0],ratings=d[2],item_name=d[3],shop_name=d[5],item_price=d[4],brand=d[6],review=d[7],time=times,date=dates,product_id=pk_id)
                obj.save()
            else:
                messages.info(request, 'Product Not Found / Product has been removed from daraz')
        except:
            messages.info(request, 'Product Not Found  / Product has been removed from daraz')
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
        products=UserProductsTracking.objects.filter(Q(sku=products.sku) | Q(product_id=products.id))
        print("sa",products)
        datalst=[]
        for i in products:
            datalst.append(int(i.stock))
        print(datalst)
        timelst=[]
        for i in products:
            timelst.append(str(i.date))
        print(timelst)
        price_lst=[]
        for i in products:
            if str(i.item_price).replace(',',''):
                item_price=str(i.item_price).replace(',','')
                item_price=str(item_price).replace('Rs. ','')
                price_lst.append(str(item_price))
            else:
                item_price=str(i.item_price).replace('Rs. ','')
                price_lst.append(str(item_price))
        print(price_lst)

        color = []
        n = len(price_lst)

        for i in range(n):
            color.append('#%06X' % randint(0, 0xFFFFFF))
        print(color)
        context={'products':products,'datalst':datalst,'timelst':timelst,'price_lst':price_lst,'color':color}
        return render(request,'PHT/product.html',context)
    else:
        products=UserScrapeData.objects.filter(id=pk)
        print("s",products) 
        datalst=[]
        for i in products:
            datalst.append(int(i.stock))
        print(datalst)
        timelst=[]
        for i in products:
            timelst.append(str(i.date))
        print(timelst)
        price_lst=[]
        for i in products:
            if str(i.item_price).replace(',',''):
                item_price=str(i.item_price).replace(',','')
                item_price=str(item_price).replace('Rs. ','')
                price_lst.append(str(item_price))
            else:
                item_price=str(i.item_price).replace('Rs. ','')
                price_lst.append(str(item_price))
        print(price_lst)
        color = []
        n = len(price_lst)

        for i in range(n):
            color.append('#%06X' % randint(0, 0xFFFFFF))
        print(color)
        context={'products':products,'datalst':datalst,'timelst':timelst,'price_lst':price_lst,'color':color}
        return render(request,'PHT/product.html',context)
    

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
        data=data[2:how+2]
        print(data)
        userid=request.user.id
        
        try:
            for urls in data:
                # options=Options()
                # options.headless=False
                # # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
                # driver = webdriver.Chrome(ChromeDriverManager().install())
                # print(urls)
                # # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
                # # url="view-source:"+urlss
                # driver.get(urls)
                # time.sleep(15)
                # # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div').click()
                # driver.execute_script("window.scrollTo(0, 1350)")
                # driver.execute_script("window.scrollTo(0, 1250)")
                # driver.execute_script("window.scrollTo(0, 1150)")
                # driver.execute_script("window.scrollTo(0, 1050)")
                # driver.execute_script("window.scrollTo(0, 1050)")
                # time.sleep(20)
                # driver.execute_script("window.scrollTo(0, 1150)")
                # driver.execute_script("window.scrollTo(0, 1250)")
                # # a=driver.find_element_by_xpath('/html/body/div[4]/div/div[8]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
                # p = driver.page_source
                # name=driver.find_element_by_xpath('//*[@id="module_product_title_1"]/div/div/span').text
                # price=driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/span').text
                # shopname=driver.find_element_by_xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a').text
                # review=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
                
                # brand=driver.find_element_by_xpath('//*[@id="module_product_brand_1"]/div/a[1]').text
                # review=review.split(" ")
                # review=review[0]
                
                # read=str(p) #Needed to do as the file encoding is undefined
                # # cap=""
                # # a=re.findall("ratings.:..average.:...",read)
                # ratings=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[3]').text
                # print(ratings)
                # skudata=re.findall("SKU.:........................",read)
                # # stockdata=re.findall("stoock.:....",read)
                # for i in skudata:
                #     skud=i[6::]
                #     print("SKU ",skud)
                #     break
                # p=re.compile(r'"stoock":(\w+)')
                # m=p.finditer(read)
                # for i in m:
                #     stock=i.group(1)
                #     print(i.group(1))
                #     break
                da=scrapedataurl(urls)
                obj=CompetitorData.objects.create(search_name=keyword,userid=userid,product_url=urls,product_title=da[3],item_price=da[4],review=da[7],product_sku=da[1],stock=da[0],ratings=da[2])
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
            
            # url = str('https://www.daraz.pk/catalog/?q=')
            # urlss=url+i.product_sku
            data=scrapedata(i.product_sku)
            # options=Options()
            # options.headless=True
            # # chrome='E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe'
            # driver = webdriver.Chrome(ChromeDriverManager().install())
            # # driver = webdriver.Chrome('E:/DJ/NEWESCOUT/ESCOUT/chromedriver.exe',chrome_options=options)
            # # url="view-source:"+urlss
            # driver.get(urlss)
            # time.sleep(15)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div').click()
            # driver.execute_script("window.scrollTo(0, 1350)")
            # driver.execute_script("window.scrollTo(0, 1250)")
            # driver.execute_script("window.scrollTo(0, 1150)")
            # driver.execute_script("window.scrollTo(0, 1050)")
            # driver.execute_script("window.scrollTo(0, 1050)")
            # time.sleep(20)
            # driver.execute_script("window.scrollTo(0, 1150)")
            # driver.execute_script("window.scrollTo(0, 1250)")
            # # a=driver.find_element_by_xpath('/html/body/div[4]/div/div[8]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
            # p = driver.page_source
            # name=driver.find_element_by_xpath('//*[@id="module_product_title_1"]/div/div/span').text
            # price=driver.find_element_by_xpath('//*[@id="module_product_price_1"]/div/div/span').text
            # shopname=driver.find_element_by_xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a').text
            # review=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]').text
            
            # brand=driver.find_element_by_xpath('//*[@id="module_product_brand_1"]/div/a[1]').text
            # review=review.split(" ")
            # review=review[0]
            # urls=driver.current_url
            # read=str(p) #Needed to do as the file encoding is undefined
            # # cap=""
            # # a=re.findall("ratings.:..average.:...",read)
            # ratings=driver.find_element_by_xpath('/html/body/div[4]/div/div[9]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[3]').text
            # print(ratings)
            # skudata=re.findall("SKU.:........................",read)
            # # stockdata=re.findall("stoock.:....",read)
            # for i in skudata:
            #     skud=i[6::]
            #     print("SKU ",skud)
            #     break
            # p=re.compile(r'"stoock":(\w+)')
            # m=p.finditer(read)
            # for i in m:
            #     stock=i.group(1)
            #     print(i.group(1))
            #     break
            # print("RATING ",ratings)
            # print("ITEM-NAME ",name)
            # print("ITEM-PRICE ",price)
            # print("SHOP-NAME ",shopname)
            # print("Review ",review)
            # print("Brand ",brand)
            # print(stock)
            userid=request.user.id
            obj=CompetitorData.objects.create(search_name=keyword,userid=userid,product_title=data[3],item_price=data[4],review=data[7],product_sku=data[1],stock=data[0],ratings=data[2])
            obj.save()


        return redirect("datacompetitor")
