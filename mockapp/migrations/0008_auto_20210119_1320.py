# Generated by Django 3.1.5 on 2021-01-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0007_auto_20210113_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testcategory',
            options={'ordering': ['category', 'keyword', 'preview_keyword', 'pub_date', 'edit_date', 'previous_year_keyword', 'preview_previous_year_keyword', 'show', 'preview_show']},
        ),
        migrations.AddField(
            model_name='testcategory',
            name='preview_previous_year_keyword',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='testcategory',
            name='preview_show',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testcategory',
            name='previous_year_keyword',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='testcategory',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]