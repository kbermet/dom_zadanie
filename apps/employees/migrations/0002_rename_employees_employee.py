# Generated by Django 3.2.5 on 2021-08-02 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employees',
            new_name='Employee',
        ),
    ]