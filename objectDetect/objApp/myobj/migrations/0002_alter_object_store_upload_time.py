# Generated by Django 3.2 on 2021-04-23 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myobj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object_store',
            name='upload_time',
            field=models.DateField(null=True),
        ),
    ]