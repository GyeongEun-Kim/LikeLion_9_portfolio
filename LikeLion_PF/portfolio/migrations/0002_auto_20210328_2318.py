# Generated by Django 3.1.7 on 2021-03-28 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='text',
            new_name='content',
        ),
    ]
