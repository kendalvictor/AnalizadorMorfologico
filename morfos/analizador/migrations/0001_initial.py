# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wikicorpus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('palabra', models.TextField()),
                ('lema', models.TextField()),
                ('tag', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
