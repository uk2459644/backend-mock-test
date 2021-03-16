# Generated by Django 3.1.5 on 2021-03-16 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mockapp', '0034_institute_keyword'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectByTestName',
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
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mockapp.city')),
                ('language', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='mockapp.languageselector')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.month')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mockapp.state')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mockapp.subject')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.year')),
            ],
            options={
                'ordering': ['test_number', 'year', 'month', 'show_test', 'user', 'is_previous_year_question', 'total_no_of_question', 'language', 'test_name', 'test_time', 'pub_date', 'edit_date', 'subject'],
            },
        ),
        migrations.CreateModel(
            name='QuestionBySubjectTestName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprehension_show', models.BooleanField(default=False)),
                ('comprehension_doc', models.BooleanField(default=False)),
                ('comprehension', models.TextField(blank=True, null=True)),
                ('show', models.BooleanField(default=True)),
                ('question_doc', models.BooleanField(default=False)),
                ('question_number', models.IntegerField(blank=True, null=True)),
                ('question', models.TextField(help_text='Write question')),
                ('doc', models.BooleanField(default=False)),
                ('a', models.TextField(help_text='Option a')),
                ('b', models.TextField(help_text='Option b')),
                ('c', models.TextField(help_text='Option c')),
                ('d', models.TextField(help_text='Option d')),
                ('correct_opt', models.CharField(max_length=1)),
                ('correct_text', models.TextField(default='', help_text='Correct option value')),
                ('correct_mark', models.FloatField(default=1)),
                ('negative_mark', models.FloatField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.testcategory')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.month')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.subject')),
                ('test_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.subjectbytestname')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mockapp.year')),
            ],
            options={
                'ordering': ['test_name', 'category', 'subject', 'month', 'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt', 'question_number', 'correct_mark', 'correct_text', 'correct_text', 'negative_mark'],
            },
        ),
    ]
