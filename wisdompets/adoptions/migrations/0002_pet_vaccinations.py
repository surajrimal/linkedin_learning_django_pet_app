# Generated by Django 3.0.3 on 2021-08-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='vaccinations',
            field=models.ManyToManyField(blank=True, to='adoptions.Vaccine'),
        ),
    ]
