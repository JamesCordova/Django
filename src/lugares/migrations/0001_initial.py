# Generated by Django 4.0.5 on 2022-06-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('nombre', models.TextField(blank=True, max_length=30)),
                ('nroTuristasYear', models.IntegerField()),
                ('pais', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]