# Generated by Django 2.1.5 on 2019-04-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20190408_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opioids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DrugName', models.TextField(null=True)),
                ('IsOpioid', models.TextField(null=True)),
            ],
        ),
    ]
