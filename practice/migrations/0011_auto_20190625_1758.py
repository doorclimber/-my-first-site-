# Generated by Django 2.2.2 on 2019-06-25 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0010_auto_20190625_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='_profile_follows_+', to='practice.profile'),
        ),
    ]
