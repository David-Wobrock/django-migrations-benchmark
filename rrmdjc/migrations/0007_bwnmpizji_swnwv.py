# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcyjx', '0011_nmbztrlh_vrbhetrjgt'),
        ('rrmdjc', '0006_remove_bwnmpizji_ryght'),
    ]

    operations = [
        migrations.AddField(
            model_name='bwnmpizji',
            name='swnwv',
            field=models.OneToOneField(on_delete=models.CASCADE, null=True, related_name='+', to='gcyjx.Xdvbgtxz'),
        ),
    ]
