# Generated by Django 2.2.2 on 2019-06-25 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0012_auto_20190625_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
    ]