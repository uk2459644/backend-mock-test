# Generated by Django 3.1.5 on 2021-03-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0032_auto_20210315_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='keyword',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='keyword',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
