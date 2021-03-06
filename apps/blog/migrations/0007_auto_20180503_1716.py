# Generated by Django 2.0.4 on 2018-05-03 17:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180503_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Content',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='category',
            name='nums',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='总数'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='nums',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='总数'),
        ),
    ]
