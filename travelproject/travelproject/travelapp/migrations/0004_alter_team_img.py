# Generated by Django 4.2.2 on 2023-06-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_rename_name_team_nam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='pic'),
        ),
    ]
