# Generated by Django 3.2.16 on 2023-01-07 10:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]