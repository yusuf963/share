# Generated by Django 4.0.4 on 2022-05-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='test',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
