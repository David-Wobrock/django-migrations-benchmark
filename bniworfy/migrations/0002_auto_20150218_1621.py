# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epbbfwihj', '0001_initial'),
        ('avwpufexob', '0001_initial'),
        ('bniworfy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sbfynkpvu',
            name='inzqctzh',
            field=models.ForeignKey(on_delete=models.CASCADE, null=True, related_name='+', to='epbbfwihj.Pbnaktpzhs'),
        ),
        migrations.AddField(
            model_name='gsmbfohda',
            name='vuszhgsx',
            field=models.OneToOneField(on_delete=models.CASCADE, null=True, related_name='+', to='avwpufexob.Fvlkcjd'),
        ),
    ]
