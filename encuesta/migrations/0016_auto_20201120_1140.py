# Generated by Django 3.0 on 2020-11-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0015_auto_20191223_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.IntegerField(choices=[(1, 'Profile'), (2, 'Skills'), (3, 'Wages'), (4, 'Other')], default=1),
        ),
    ]