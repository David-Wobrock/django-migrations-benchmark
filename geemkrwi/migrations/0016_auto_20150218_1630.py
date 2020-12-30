# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakry', '0015_auto_20150218_1630'),
        ('geemkrwi', '0015_hxkigetost_gvsmh'),
    ]

    run_before = [
        ('ysgxuyu', '0012_delete_bmovnbnmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uqqgcprwn',
            name='cordori',
        ),
        migrations.RemoveField(
            model_name='wilsmoea',
            name='ninajhwzfe',
        ),
        migrations.AddField(
            model_name='knrrd',
            name='hwqsq',
            field=models.OneToOneField(on_delete=models.CASCADE, null=True, related_name='+', to='kakry.Wnbhmzvze'),
        ),
        migrations.AddField(
            model_name='uqqgcprwn',
            name='birbvhypj',
            field=models.CharField(default='', max_length=1),
        ),
    ]
