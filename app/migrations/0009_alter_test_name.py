# Generated by Django 4.2.3 on 2023-07-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_test_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=2, null=True, unique=True),
        ),
    ]
