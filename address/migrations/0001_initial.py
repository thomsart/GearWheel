# Generated by Django 3.2 on 2021-05-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('longitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('start', models.BooleanField(default=False)),
                ('end', models.BooleanField(default=False)),
                ('stop', models.BooleanField(default=False)),
            ],
        ),
    ]
