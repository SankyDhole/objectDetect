# Generated by Django 3.2 on 2021-04-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='object_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100, null=True)),
                ('object_detail', models.JSONField(null=True)),
                ('upload_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='uploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_file', models.FileField(upload_to='')),
                ('img_file', models.ImageField(upload_to='')),
            ],
        ),
    ]
