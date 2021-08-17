# Generated by Django 3.2.6 on 2021-08-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oredermodel',
            name='city',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='state',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='street',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]