# Generated by Django 2.1.5 on 2019-04-08 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20190408_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qty', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctordrug',
            name='DrugName',
        ),
        migrations.AddField(
            model_name='doctor',
            name='DoctorID',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='DoctorDrug',
        ),
        migrations.AddField(
            model_name='drugdoctor',
            name='DoctorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Doctor'),
        ),
        migrations.AddField(
            model_name='drugdoctor',
            name='DrugName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Drug'),
        ),
    ]
