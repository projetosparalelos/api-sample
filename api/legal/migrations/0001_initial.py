# Generated by Django 2.2.2 on 2019-06-29 13:02

import uuid

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Legal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('language', models.CharField(choices=[('en-US', 'English (US)'), ('es-ES', 'Español (España)'), ('pt-BR', 'Português (Brasil)')], db_index=True, max_length=16, verbose_name='language')),
                ('type', models.CharField(choices=[('about', 'About'), ('privacy', 'Privacy'), ('terms', 'Terms')], max_length=16, verbose_name='type')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
            ],
            options={
                'verbose_name': 'legal',
                'verbose_name_plural': 'legal',
            },
        ),
    ]
