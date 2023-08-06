# Generated by Django 4.2.4 on 2023-08-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('hspw', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meigen_app.group')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meigen_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Meigener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meigen_app.group')),
            ],
        ),
        migrations.CreateModel(
            name='Meigen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meigen', models.CharField(max_length=1024)),
                ('meigener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meigen_app.meigener')),
            ],
        ),
    ]
