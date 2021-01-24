# Generated by Django 3.1.5 on 2021-01-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0014_auto_20210123_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biharpolicetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearrrbgroupdtestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearrrbntpctestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearssccgltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearsscchsltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearsscjecetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearsscjeeetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='rrbgroupdtestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='rrbntpctestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='ssccgltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscchsltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscjecetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscjeeetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AddField(
            model_name='biharpolicetestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='previousyearrrbgroupdtestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='previousyearrrbntpctestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='previousyearssccgltestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='previousyearsscchsltestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='previousyearsscjecetestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='previousyearsscjeeetestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='rrbgroupdtestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='rrbntpctestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='ssccgltestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='sscchsltestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='sscjecetestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
        migrations.AddField(
            model_name='sscjeeetestname',
            name='test_time',
            field=models.IntegerField(default=60, help_text='test time in minutes'),
        ),
    ]