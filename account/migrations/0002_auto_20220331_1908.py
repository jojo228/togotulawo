# Generated by Django 3.2.4 on 2022-03-31 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auteur',
            name='annee_graduation',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='image',
            field=models.ImageField(blank=True, default='profile2.png', null=True, upload_to='files/profic_pic'),
        ),
    ]
