# Generated by Django 4.2.4 on 2023-08-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meigen_app', '0002_alter_group_table_alter_meigen_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hspw',
            field=models.CharField(max_length=128),
        ),
    ]