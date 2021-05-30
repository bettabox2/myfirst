# Generated by Django 3.2.3 on 2021-05-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v2', '0004_raid'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('fraction', models.CharField(max_length=40)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]
