# Generated by Django 4.2.4 on 2023-09-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_course_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=20),
        ),
    ]
