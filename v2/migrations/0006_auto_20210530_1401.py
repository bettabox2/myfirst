# Generated by Django 3.2.3 on 2021-05-30 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v2', '0005_heroclass_race'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeroClass',
        ),
        migrations.DeleteModel(
            name='Profession',
        ),
        migrations.DeleteModel(
            name='Race',
        ),
        migrations.DeleteModel(
            name='Raid',
        ),
    ]
