# Generated by Django 3.2.9 on 2021-11-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='size',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]