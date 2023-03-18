# Generated by Django 4.1.3 on 2022-12-14 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewr_name', models.CharField(max_length=65)),
                ('review_title', models.CharField(max_length=100)),
                ('tasl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.task')),
            ],
        ),
    ]
