# Generated by Django 4.1.4 on 2023-06-08 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foliomine', '0004_project_project_code_link_project_project_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='end_date',
            new_name='edu_end_date',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='end_date',
            new_name='exp_end_date',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='start_date',
            new_name='exp_start_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='end_date',
            new_name='proj_end_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='start_date',
            new_name='proj_start_date',
        ),
    ]