# Generated by Django 5.1.6 on 2025-02-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0003_alter_projectimages_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimages',
            name='image',
            field=models.ImageField(upload_to='project_images'),
        ),
    ]
