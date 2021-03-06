# Generated by Django 4.0.4 on 2022-05-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kluby', '0003_klub_nation_alter_competition_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(help_text='Enter a club competition (e.g. Champions league, LaLiga)', max_length=50, unique=True, verbose_name='Competition name'),
        ),
    ]
