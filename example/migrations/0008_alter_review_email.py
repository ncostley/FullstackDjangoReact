# Generated by Django 5.0.7 on 2024-07-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0007_recipe_type_alter_review_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
