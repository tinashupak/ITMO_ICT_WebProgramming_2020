# Generated by Django 3.0.4 on 2020-04-20 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0013_auto_20200420_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AddField(
            model_name='comment',
            name='datein',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='dateout',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
