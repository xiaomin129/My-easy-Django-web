# Generated by Django 4.1.2 on 2022-11-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_rename_userinfo_workerinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerinfo',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]