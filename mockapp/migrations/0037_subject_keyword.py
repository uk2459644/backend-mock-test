# Generated by Django 3.1.5 on 2021-03-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0036_auto_20210316_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='keyword',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
