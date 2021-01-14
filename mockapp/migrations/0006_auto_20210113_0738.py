# Generated by Django 3.1.5 on 2021-01-13 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0005_auto_20210112_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='languageselector',
            options={'ordering': ['lang_name', 'lang_no', 'show']},
        ),
        migrations.AddField(
            model_name='languageselector',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]