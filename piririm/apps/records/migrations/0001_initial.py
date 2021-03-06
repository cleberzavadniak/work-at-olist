# Generated by Django 2.2.1 on 2019-05-01 18:10

from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallEndRecord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=utils.models.ulid_str_generator, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('call_id', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CallStartRecord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=utils.models.ulid_str_generator, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('call_id', models.PositiveIntegerField()),
                ('source', models.CharField(max_length=11)),
                ('destination', models.CharField(max_length=11)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
