# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zsskgviadw', '0002_auto_20150218_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inyvz',
            name='nqrrfjy',
        ),
        migrations.AddField(
            model_name='hcetattb',
            name='lcdqnzq',
            field=models.IntegerField(default=0),
        ),
        #migrations.DeleteModel(
        #    name='Inyvz',
        #),
    ]
