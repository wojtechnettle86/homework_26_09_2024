# Generated by Django 5.1.1 on 2024-09-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
