# Generated by Django 4.0.4 on 2022-05-18 15:59

from django.db import migrations, models
import sampleworks.models.works


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
                ('thumb_nail', models.ImageField(upload_to=sampleworks.models.works.get_file_path)),
                ('description', models.TextField()),
                ('owner', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
