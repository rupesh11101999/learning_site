# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20171129_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.IntegerField(default=0)),
                ('prompt', models.TextField()),
                ('quiz', models.ForeignKey(to='courses.Quiz')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
