# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxxavsovs', '0012_kxgenek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kxgenek',
            name='rgnvvw',
        ),
        migrations.AddField(
            model_name='kxgenek',
            name='lbqqlez',
            field=models.IntegerField(default=0),
        ),
    ]
