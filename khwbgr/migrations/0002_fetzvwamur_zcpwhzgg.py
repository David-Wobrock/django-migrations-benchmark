# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkfudme', '0001_initial'),
        ('khwbgr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fetzvwamur',
            name='zcpwhzgg',
            field=models.ForeignKey(on_delete=models.CASCADE, null=True, related_name='+', to='pkfudme.Dbpile'),
        ),
    ]
