# Generated by Django 3.0.5 on 2020-04-25 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_auto_20200425_2112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Стаття', 'verbose_name_plural': 'Статті'},
        ),
    ]
