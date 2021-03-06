# Generated by Django 3.0.11 on 2021-02-08 16:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=5000, verbose_name='Describe the Hackathon')),
                ('evaluation', models.TextField(max_length=5000, verbose_name='Describe how will the hackathon be evaluated')),
                ('timeline', models.TextField(max_length=5000, verbose_name="Describe the Hackathon's timeline")),
                ('rules', models.TextField(max_length=5000, verbose_name='Describe rules for the hackathon')),
                ('prizes', models.TextField(max_length=5000, verbose_name='Describe how the prize money will be distributed')),
                ('prize_money', models.PositiveIntegerField(default=0, verbose_name='Total prize money')),
                ('date_start', models.DateField(verbose_name='Hackathon start date')),
                ('date_end', models.DateField(verbose_name='Hackathon end date')),
                ('competitors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
