# Generated by Django 3.2.7 on 2022-05-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PHT', '0003_darazalldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='darazalldata',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
