# Generated by Django 4.2.3 on 2023-08-07 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_book_user_book_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='b',
            name='test',
        ),
        migrations.RemoveField(
            model_name='b',
            name='test2',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='c',
            name='test',
        ),
        migrations.RemoveField(
            model_name='c',
            name='test2',
        ),
        migrations.RemoveField(
            model_name='pupil',
            name='school',
        ),
        migrations.DeleteModel(
            name='shit',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sponsors',
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='legal_entity',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.DeleteModel(
            name='B',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='C',
        ),
        migrations.DeleteModel(
            name='Pupil',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='Test2',
        ),
    ]
