# Generated by Django 4.0.4 on 2022-05-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, choices=[('NEW', 'Newcastle'), ('SAMP', 'Southampton'), ('WINCH', 'Winchester'), ('CAMB', 'Cambridge'), ('LIV', 'Liverpool'), ('LOND', 'London'), ('POR', 'Portsmouth'), ('MANCH', 'Manchester'), ('BRIS', 'Bristol'), ('HULL', 'Hull')], default='LOND', max_length=50, null=True),
        ),
    ]
