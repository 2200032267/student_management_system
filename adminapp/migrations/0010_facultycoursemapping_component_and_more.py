# Generated by Django 4.2.4 on 2023-09-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_course_credits_course_ltps_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultycoursemapping',
            name='component',
            field=models.CharField(choices=[('L', 'Lecture'), ('T', 'Tutorial'), ('P', 'Pratical'), ('S', 'Skill')], default='L', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facultycoursemapping',
            name='section',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facultycoursemapping',
            name='type',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
