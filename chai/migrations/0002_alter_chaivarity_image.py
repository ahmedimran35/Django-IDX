# Generated by Django 5.0.6 on 2024-05-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaivarity',
            name='image',
            field=models.ImageField(upload_to='chais/'),
        ),
    ]