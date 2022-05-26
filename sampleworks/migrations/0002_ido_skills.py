# Generated by Django 4.0.4 on 2022-05-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleworks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
                ('short_description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('percent', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
