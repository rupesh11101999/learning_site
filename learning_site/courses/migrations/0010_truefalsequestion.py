# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_multiplechoicequestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='courses.Question')),
            ],
            bases=('courses.question',),
        ),
    ]
