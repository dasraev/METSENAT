# Generated by Django 4.2.3 on 2023-07-31 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_b_name2_b_name3_b_name4_b_noname_b_test_b_test2_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]