# Generated by Django 3.1.2 on 2020-10-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='log_db',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]