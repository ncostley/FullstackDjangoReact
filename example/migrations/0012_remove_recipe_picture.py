# Generated by Django 5.0.7 on 2024-07-19 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0011_recipe_picture_alter_review_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='picture',
        ),
    ]
