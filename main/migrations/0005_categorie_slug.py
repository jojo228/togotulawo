# Generated by Django 3.2.4 on 2022-04-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_article_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(default=0, max_length=300, unique=True),
            preserve_default=False,
        ),
    ]
