# Generated by Django 4.0.4 on 2022-06-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date_extraction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateextraction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
