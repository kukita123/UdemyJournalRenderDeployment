# Generated by Django 4.1.3 on 2022-12-14 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='tasl',
            new_name='task',
        ),
    ]