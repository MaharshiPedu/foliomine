# Generated by Django 4.1.4 on 2023-06-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foliomine', '0003_profile_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_code_link',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_photo',
            field=models.ImageField(blank=True, null=True, upload_to='project_photos/%Y/%m/%d/'),
        ),
    ]