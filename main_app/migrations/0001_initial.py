# Generated by Django 4.1.2 on 2022-10-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=250)),
                ('esrb_rating', models.CharField(max_length=5)),
            ],
        ),
    ]