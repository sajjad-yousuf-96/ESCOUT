# Generated by Django 3.2.7 on 2022-05-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PHT', '0007_auto_20220524_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='categoryrecords',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='commissionlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userscrapedata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
