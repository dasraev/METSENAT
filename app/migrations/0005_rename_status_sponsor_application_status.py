# Generated by Django 4.2.3 on 2023-07-28 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_test2_alter_test_asd_b'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='status',
            new_name='application_status',
        ),
    ]
