# Generated by Django 4.2.2 on 2023-06-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='identifier',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
