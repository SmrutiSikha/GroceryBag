# Generated by Django 3.1.4 on 2021-01-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210108_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='ItemStatus',
            field=models.CharField(max_length=15),
        ),
    ]
