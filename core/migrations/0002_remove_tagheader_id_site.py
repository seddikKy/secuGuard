# Generated by Django 4.1.4 on 2022-12-20 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagheader',
            name='id_Site',
        ),
    ]