# Generated by Django 2.0.7 on 2018-08-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qyulzung', '0005_auto_20180807_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criteria',
            old_name='alternatives',
            new_name='alt',
        ),
        migrations.AddField(
            model_name='qz',
            name='cr1',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='qz',
            name='cr2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='qz',
            name='cr3',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
