# Generated by Django 4.2.10 on 2024-03-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_remove_subscribe_option_subscribe_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='options',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='M', max_length=2),
        ),
    ]
