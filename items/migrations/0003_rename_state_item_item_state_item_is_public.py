# Generated by Django 4.0.4 on 2022-05-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_rename_image_item_hero_image_item_image1_item_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='state',
            new_name='item_state',
        ),
        migrations.AddField(
            model_name='item',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
