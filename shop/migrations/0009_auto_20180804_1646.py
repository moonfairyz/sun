# Generated by Django 2.0.7 on 2018-08-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20180804_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]