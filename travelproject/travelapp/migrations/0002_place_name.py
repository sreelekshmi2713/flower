# Generated by Django 3.2.15 on 2022-08-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='name',
            field=models.CharField(default='', max_length=140, null=True),
        ),
    ]