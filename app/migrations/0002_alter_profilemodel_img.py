# Generated by Django 3.2.8 on 2021-11-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='img',
            field=models.ImageField(upload_to='profileimg'),
        ),
    ]