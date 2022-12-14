# Generated by Django 3.2.11 on 2022-08-22 21:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20220823_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAfter',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-create_at'],
                'abstract': False,
            },
        ),
    ]
