# Generated by Django 2.1.5 on 2019-04-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_prescriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriber',
            name='OpioidPrescriber',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='prescriber',
            name='TotalPrescriptions',
            field=models.TextField(null=True),
        ),
    ]
