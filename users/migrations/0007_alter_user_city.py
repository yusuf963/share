# Generated by Django 4.0.4 on 2022-05-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, choices=[('HULL', 'Hull'), ('LIV', 'Liverpool'), ('CAMB', 'Cambridge'), ('MANCH', 'Manchester'), ('NEW', 'Newcastle'), ('WINCH', 'Winchester'), ('BRIS', 'Bristol'), ('POR', 'Portsmouth'), ('LOND', 'London'), ('SAMP', 'Southampton')], default='LOND', max_length=50, null=True),
        ),
    ]
