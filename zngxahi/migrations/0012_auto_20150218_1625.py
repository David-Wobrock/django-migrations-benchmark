# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qqpppzas', '0011_auto_20150218_1625'),
        ('rwlfplwktj', '0007_yjzzdopc'),
        ('zngxahi', '0011_auto_20150218_1625'),
    ]

    run_before = [
        ('qqpppzas', '0012_auto_20150218_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdontoyqti',
            name='wjquqibaq',
        ),
        migrations.RemoveField(
            model_name='llnksobygh',
            name='xjfzzpp',
        ),
        migrations.RemoveField(
            model_name='nnkqr',
            name='wcytnskou',
        ),
        migrations.AddField(
            model_name='bdontoyqti',
            name='ywvylo',
            field=models.ForeignKey(on_delete=models.CASCADE, null=True, related_name='+', to='rwlfplwktj.Thqldbdjm'),
        ),
        migrations.AddField(
            model_name='dhynhe',
            name='nikevgkpn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='llnksobygh',
            name='mfhovgyh',
            field=models.ForeignKey(on_delete=models.CASCADE, null=True, related_name='+', to='qqpppzas.Xcuutwsyfn'),
        ),
        migrations.AddField(
            model_name='nxqpxgzt',
            name='mtarxlfyow',
            field=models.CharField(default='', max_length=82),
        ),
    ]
