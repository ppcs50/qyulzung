# Generated by Django 2.0.7 on 2018-08-08 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qyulzung', '0008_auto_20180807_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='qz',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]