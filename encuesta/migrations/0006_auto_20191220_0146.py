# Generated by Django 3.0 on 2019-12-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0005_auto_20191220_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='education',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='seniority',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
