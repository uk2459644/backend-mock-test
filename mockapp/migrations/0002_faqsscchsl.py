# Generated by Django 3.1.5 on 2021-01-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQSSCChsl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_no', models.IntegerField()),
                ('faq_question', models.CharField(help_text='FAQ Question', max_length=150)),
                ('faq_answer', models.TextField(help_text='Answer here .')),
                ('show', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['faq_no', 'faq_question', 'faq_answer', 'show'],
            },
        ),
    ]
