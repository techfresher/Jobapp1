# Generated by Django 4.2.10 on 2024-02-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_jobpost_salary_alter_jobpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='expire',
            field=models.DateField(null=True),
        ),
    ]
