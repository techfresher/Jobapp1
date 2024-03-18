# Generated by Django 4.2.10 on 2024-02-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(max_length=30, null=True, unique=True),
        ),
    ]
