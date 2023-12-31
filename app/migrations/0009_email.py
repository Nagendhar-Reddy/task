# Generated by Django 4.2.6 on 2023-11-17 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('recipient', models.EmailField(max_length=254)),
            ],
        ),
    ]
