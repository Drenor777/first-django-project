# Generated by Django 3.2.7 on 2021-10-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0004_alter_film_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
    ]