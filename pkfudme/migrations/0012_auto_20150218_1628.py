# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geemkrwi', '0014_auto_20150218_1628'),
        ('pkfudme', '0011_remove_ewxxluebq_sqyiv'),
    ]

    run_before = [
        ('geemkrwi', '0018_auto_20150218_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='fkazepju',
            name='hwxuvu',
            field=models.OneToOneField(on_delete=models.CASCADE, null=True, related_name='+', to='geemkrwi.Uqqgcprwn'),
        ),
        migrations.AddField(
            model_name='heehdxfqyb',
            name='xobdnqb',
            field=models.CharField(default='', max_length=236),
        ),
    ]
