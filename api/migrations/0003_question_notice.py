# Generated by Django 3.2.2 on 2021-08-17 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210817_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='notice',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=5),
        ),
    ]
