# Generated by Django 2.0.7 on 2018-08-05 17:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('alternatives', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='qyulzung.Alternative')),
            ],
        ),
        migrations.CreateModel(
            name='QZ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=128)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Time')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='alternative',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='qyulzung.QZ'),
        ),
    ]
