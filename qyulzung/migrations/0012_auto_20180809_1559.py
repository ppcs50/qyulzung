# Generated by Django 2.0.7 on 2018-08-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qyulzung', '0011_auto_20180809_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='criteria',
            name='user',
        ),
        migrations.DeleteModel(
            name='Criteria',
        ),
    ]
