# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irmtbds', '0003_rqzheruyb_dzqlaunuix'),
        ('zhavbmq', '0003_auto_20150218_1621'),
    ]

    run_before = [
        ('irmtbds', '0004_auto_20150218_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmaopvcufb',
            name='vabnk',
            field=models.ForeignKey(on_delete=models.CASCADE, null=True, related_name='+', to='irmtbds.Rqzheruyb'),
        ),
    ]
