# Generated by Django 4.2.10 on 2024-03-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_subscribe_option_alter_subscribe_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='option',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='options',
            field=models.EmailField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='W', max_length=2),
            preserve_default=False,
        ),
    ]