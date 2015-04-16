# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=models.CharField(default=b'W', max_length=1, choices=[(b'R', b'Red'), (b'B', b'Blue'), (b'O', b'Orange'), (b'Y', b'Yellow'), (b'G', b'Gray'), (b'W', b'White')]),
        ),
    ]
