# Generated by Django 3.1.5 on 2021-02-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='realtor',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='realtor',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]