# Generated by Django 3.0.4 on 2020-05-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=3.5, max_digits=3),
        ),
    ]
