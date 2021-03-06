# Generated by Django 3.0.5 on 2020-04-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_auto_20200425_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(help_text='Максимум 250 символів', max_length=250, verbose_name='Домашнє завдання')),
                ('slug', models.SlugField(blank=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Домашнє завдання',
                'verbose_name_plural': 'Категорії для публікацій',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Додати публікацію', 'verbose_name_plural': 'Статті'},
        ),
    ]
