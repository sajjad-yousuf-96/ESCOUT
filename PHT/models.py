from datetime import date
from django.db import models

# Create your models here.

class UserScrapeData(models.Model):
    userid=models.CharField(max_length=200,null=True)
    sku=models.CharField(max_length=200,null=True)
    stock=models.CharField(max_length=200,null=True)
    # date_created=models.CharField(auto_now_add=True,null=True)
    ratings=models.CharField(max_length=200,null=True)
    item_name=models.CharField(max_length=200,null=True)
    shop_name=models.CharField(max_length=200,null=True)
    item_price=models.CharField(max_length=200,null=True)
    brand=models.CharField(max_length=200,null=True)
    review=models.CharField(max_length=200,null=True)
    time=models.CharField(max_length=200,null=True)
    date=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.item_name

class CommissionList(models.Model):
    category=models.CharField(max_length=200,null=True)
    commissions=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.category
class Categories(models.Model):
    # category_id=models.CharField(max_length=200,null=True)
    category_name=models.CharField(max_length=200,null=True)

class CategoryRecords(models.Model):
    product_sku=models.CharField(max_length=200,null=True)
    product_url=models.CharField(max_length=200,null=True)
    product_title=models.CharField(max_length=200,null=True)
    product_price=models.CharField(max_length=200,null=True)
    product_review=models.CharField(max_length=200,null=True)
    product_rating=models.CharField(max_length=200,null=True)
    # category_id=models.ForeignKey(Categories,null=True,on_delete=models.CASCADE)
    category_name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.category_name
class CompetitorData(models.Model):
    userid=models.CharField(max_length=200,null=True)
    search_name=models.CharField(max_length=200,null=True)
    product_sku=models.CharField(max_length=200,null=True)
    product_url=models.CharField(max_length=200,null=True)
    product_title=models.CharField(max_length=200,null=True)
    stock=models.CharField(max_length=200,null=True)
    ratings=models.CharField(max_length=200,null=True)
    item_price=models.CharField(max_length=200,null=True)
    review=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.product_sku
    
class UserProductsTracking(models.Model):
    userid=models.CharField(max_length=200,null=True)
    sku=models.CharField(max_length=200,null=True)
    stock=models.CharField(max_length=200,null=True)
    # date_created=models.CharField(auto_now_add=True,null=True)
    ratings=models.CharField(max_length=200,null=True)
    item_name=models.CharField(max_length=200,null=True)
    shop_name=models.CharField(max_length=200,null=True)
    item_price=models.CharField(max_length=200,null=True)
    brand=models.CharField(max_length=200,null=True)
    review=models.CharField(max_length=200,null=True)
    product_id=models.CharField(max_length=200,null=True)
    time=models.CharField(max_length=200,null=True)
    date=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.sku
    
class CsvSaveFile(models.Model):
    userid=models.CharField(max_length=200,null=True)
    csvfile=models.FileField(upload_to='csv_files', max_length=254)