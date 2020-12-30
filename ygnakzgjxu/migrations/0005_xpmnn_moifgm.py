# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esznwrr', '0001_initial'),
        ('ygnakzgjxu', '0004_xdwhlpqgw'),
    ]

    run_before = [
        ('esznwrr', '0004_delete_vppjpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='xpmnn',
            name='moifgm',
            field=models.ForeignKey(on_delete=models.CASCADE, null=True, related_name='+', to='esznwrr.Vppjpa'),
        ),
    ]
