# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulegwfs', '0005_auto_20150218_1623'),
        ('avwpufexob', '0009_aunuwoo'),
    ]

    run_before = [
        ('wulegwfs', '0006_delete_xcasayyn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fvlkcjd',
            name='onlvfzdsk',
        ),
        migrations.AddField(
            model_name='fvlkcjd',
            name='psxjvm',
            field=models.ForeignKey(on_delete=models.CASCADE, null=True, related_name='+', to='wulegwfs.Xcasayyn'),
        ),
    ]
