# Generated by Django 2.0.4 on 2018-05-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180502_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='logo',
            field=models.ImageField(default='logo\\default.jpg', max_length=200, upload_to='logo/', verbose_name='头像标志'),
        ),
    ]