# Generated by Django 3.2.3 on 2021-05-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_auto_20210526_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
