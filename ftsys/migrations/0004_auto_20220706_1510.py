# Generated by Django 3.1.6 on 2022-07-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftsys', '0003_auto_20220706_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='programID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
