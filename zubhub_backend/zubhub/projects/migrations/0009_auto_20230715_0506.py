# Generated by Django 3.2 on 2023-07-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_inspired_from_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(to='projects.Category'),
        ),
    ]