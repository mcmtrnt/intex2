# Generated by Django 2.1.5 on 2019-04-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DoctorID', models.IntegerField(null=True)),
                ('Fname', models.TextField(null=True)),
                ('Lname', models.TextField(null=True)),
                ('Gender', models.TextField(null=True)),
                ('State', models.TextField(null=True)),
                ('Credentials', models.TextField(null=True)),
                ('Specialty', models.TextField(null=True)),
            ],
        ),
    ]
