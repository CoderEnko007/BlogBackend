# Generated by Django 2.0.4 on 2018-05-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180506_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='md_content',
            field=models.TextField(blank=True, null=True, verbose_name='MarkDown内容'),
        ),
    ]
