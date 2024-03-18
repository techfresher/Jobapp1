# Generated by Django 4.2.10 on 2024-02-26 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('salary', models.IntegerField(default=0)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]
