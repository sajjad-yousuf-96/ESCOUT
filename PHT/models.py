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

    def __str__(self):
        return self.item_name

class CommissionList(models.Model):
    category=models.CharField(max_length=200,null=True)
    commissions=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.commissions