# Generated by Django 4.1.1 on 2022-09-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ("name", models.CharField(max_length=200)),
                ("surname", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=20)), 
                ("salary", models.IntegerField()),
            ],
        ),
    ]
