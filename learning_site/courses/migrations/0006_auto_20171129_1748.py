# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_quit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('total_questions', models.IntegerField(default=4)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.RemoveField(
            model_name='quit',
            name='course',
        ),
        migrations.DeleteModel(
            name='Quit',
        ),
    ]
