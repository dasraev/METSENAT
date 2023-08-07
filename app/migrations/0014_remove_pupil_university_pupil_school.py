# Generated by Django 4.2.3 on 2023-08-04 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_school_pupil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupil',
            name='university',
        ),
        migrations.AddField(
            model_name='pupil',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.school'),
        ),
    ]