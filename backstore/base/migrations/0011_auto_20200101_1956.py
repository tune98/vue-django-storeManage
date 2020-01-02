# Generated by Django 2.2.5 on 2020-01-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20200101_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='meterage',
        ),
        migrations.AddField(
            model_name='material',
            name='meterage_name',
            field=models.CharField(default=1, max_length=20, verbose_name='计量单位名称'),
            preserve_default=False,
        ),
    ]