# Generated by Django 4.2.4 on 2023-09-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_alter_faculty_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studentid',
            new_name='Studentid',
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=20),
        ),
    ]
