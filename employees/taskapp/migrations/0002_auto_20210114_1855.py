# Generated by Django 2.2.17 on 2021-01-14 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Role',
        ),
    ]