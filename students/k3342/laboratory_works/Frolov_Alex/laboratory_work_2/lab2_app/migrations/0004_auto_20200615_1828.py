# Generated by Django 3.0.5 on 2020-06-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab2_app', '0003_auto_20200615_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nclass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nclass', to='lab2_app.Teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('student', 'subject', 'grade')},
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together={('nclass_name', 'lesson', 'day')},
        ),
    ]
