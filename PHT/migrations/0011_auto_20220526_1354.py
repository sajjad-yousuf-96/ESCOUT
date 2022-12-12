# Generated by Django 3.2.7 on 2022-05-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PHT', '0010_auto_20220524_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProductsTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200, null=True)),
                ('sku', models.CharField(max_length=200, null=True)),
                ('stock', models.CharField(max_length=200, null=True)),
                ('ratings', models.CharField(max_length=200, null=True)),
                ('item_name', models.CharField(max_length=200, null=True)),
                ('shop_name', models.CharField(max_length=200, null=True)),
                ('item_price', models.CharField(max_length=200, null=True)),
                ('brand', models.CharField(max_length=200, null=True)),
                ('review', models.CharField(max_length=200, null=True)),
                ('product_id', models.CharField(max_length=200, null=True)),
                ('time', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userscrapedata',
            name='done',
        ),
        migrations.AddField(
            model_name='userscrapedata',
            name='date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userscrapedata',
            name='time',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
