# Generated by Django 3.1.5 on 2021-03-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0031_auto_20210315_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
