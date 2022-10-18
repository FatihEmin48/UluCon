# Generated by Django 3.2 on 2021-04-13 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('converters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='converter',
            name='link',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Converter Url'),
            preserve_default=False,
        ),
    ]