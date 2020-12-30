# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glcmkwkzv', '0003_auto_20150218_1621'),
        ('cuspknbh', '0002_auto_20150218_1621'),
        ('zngxahi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orofu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciuhnrivc', models.OneToOneField(on_delete=models.CASCADE, null=True, related_name='+', to='glcmkwkzv.Unnork')),
            ],
        ),
        migrations.AddField(
            model_name='bdontoyqti',
            name='jwrsyvtia',
            field=models.OneToOneField(on_delete=models.CASCADE, null=True, related_name='+', to='cuspknbh.Djbbtxk'),
        ),
    ]
