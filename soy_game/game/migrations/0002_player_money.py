# Generated by Django 4.1.3 on 2022-11-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='money',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
