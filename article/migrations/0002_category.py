# Generated by Django 3.1.4 on 2020-12-08 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
    ]
