# Generated by Django 5.0.7 on 2024-07-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(default=''),
        ),
    ]
