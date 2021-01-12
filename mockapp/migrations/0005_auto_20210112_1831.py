# Generated by Django 3.1.5 on 2021-01-12 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0004_rrbgroupdtestname_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='previousyearrrbgroupdtestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearrrbntpctestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearssccgltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearsscchsltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearsscjecetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='previousyearsscjeeetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='rrbgroupdtestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='rrbntpctestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='ssccgltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscchsltestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscjecetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AlterModelOptions(
            name='sscjeeetestname',
            options={'ordering': ['test_number', 'year', 'month', 'show_test', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'pub_date', 'edit_date', 'category']},
        ),
        migrations.AddField(
            model_name='previousyearrrbgroupdtestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='previousyearrrbntpctestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='previousyearssccgltestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='previousyearsscchsltestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='previousyearsscjecetestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='previousyearsscjeeetestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='rrbntpctestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='ssccgltestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='sscchsltestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='sscjecetestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
        migrations.AddField(
            model_name='sscjeeetestname',
            name='language',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector'),
        ),
    ]
