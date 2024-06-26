# Generated by Django 5.0.6 on 2024-05-30 08:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chaivarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chaivarity_images/')),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cha_type', models.CharField(choices=[('ML', 'Masala Tea'), ('GN', 'Ginger Tea'), ('LM', 'Leamon Tea'), ('RT', 'Raw Tea')], max_length=2)),
            ],
        ),
    ]
