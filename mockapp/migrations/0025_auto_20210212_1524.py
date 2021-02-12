# Generated by Django 3.1.5 on 2021-02-12 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mockapp', '0024_jobinfo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biharpolicetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='jobinfo',
            options={'ordering': ['pub_date', 'title', 'short_description', 'category', 'category_job', 'cat_text', 'month', 'year', 'image', 'info_no', 'keyword', 'show', 'user']},
        ),
        migrations.AlterModelOptions(
            name='rrbgroupdtestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='rrbntpctestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='ssccgltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscchsltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscjecetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscjeeetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AddField(
            model_name='biharpolicetestname',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rrbgroupdtestname',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rrbntpctestname',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ssccgltestname',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sscchsltestname',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sscjecetestname',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sscjeeetestname',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
