# Generated by Django 4.2.2 on 2023-06-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test1', models.CharField(max_length=10)),
            ],
        ),
    ]
