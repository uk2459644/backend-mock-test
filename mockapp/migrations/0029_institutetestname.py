# Generated by Django 3.1.5 on 2021-03-14 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mockapp', '0028_institute'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstituteTestName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_number', models.IntegerField(blank=True, null=True)),
                ('test_name', models.CharField(max_length=120)),
                ('keyword', models.CharField(blank=True, max_length=120, null=True)),
                ('is_previous_year_question', models.BooleanField(default=False)),
                ('total_no_of_question', models.IntegerField(blank=True, null=True)),
                ('pub_date', models.DateField()),
                ('edit_date', models.DateField()),
                ('show_test', models.BooleanField(default=True)),
                ('test_time', models.IntegerField(default=60, help_text='test time in minutes')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.testcategory')),
                ('institute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mockapp.institute')),
                ('language', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.month')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.year')),
            ],
            options={
                'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'category'],
            },
        ),
    ]
