# Generated by Django 3.1.5 on 2021-02-10 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0022_auto_20210206_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobinfo',
            options={'ordering': ['pub_date', 'title', 'short_description', 'category', 'category_job', 'cat_text', 'month', 'year', 'image', 'info_no', 'keyword', 'show']},
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='category_job',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mockapp.jobcategory'),
        ),
    ]