# Generated by Django 3.1.4 on 2021-01-08 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='ItemName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='ItemQuantity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='UserId',
            field=models.IntegerField(default=5),
        ),
    ]
