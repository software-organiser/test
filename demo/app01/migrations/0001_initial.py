# Generated by Django 3.1.2 on 2020-10-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chinainfo',
            fields=[
                ('year', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=30)),
                ('per', models.CharField(max_length=20)),
            ],
        ),
    ]
