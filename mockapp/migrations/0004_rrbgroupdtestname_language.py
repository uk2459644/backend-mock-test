# Generated by Django 3.1.5 on 2021-01-12 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0003_auto_20210112_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='rrbgroupdtestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
    ]