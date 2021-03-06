# Generated by Django 3.2.7 on 2022-05-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PHT', '0008_auto_20220524_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_sku', models.CharField(max_length=200, null=True)),
                ('product_url', models.CharField(max_length=200, null=True)),
                ('product_title', models.CharField(max_length=200, null=True)),
                ('stock', models.CharField(max_length=200, null=True)),
                ('ratings', models.CharField(max_length=200, null=True)),
                ('item_price', models.CharField(max_length=200, null=True)),
                ('review', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
