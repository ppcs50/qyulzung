# Generated by Django 2.0.7 on 2018-08-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qyulzung', '0010_qz_post_yn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='alternative',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Alternative',
        ),
    ]