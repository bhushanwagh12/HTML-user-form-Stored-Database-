# Generated by Django 2.0 on 2019-08-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_no', models.IntegerField()),
                ('e_name', models.CharField(max_length=20)),
                ('e_city', models.CharField(max_length=20)),
            ],
        ),
    ]
