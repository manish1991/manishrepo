# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publication', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('hero_image', models.CharField(max_length=100)),
                ('optional_image', models.CharField(max_length=100)),
                ('body_text', models.TextField()),
            ],
        ),
    ]
