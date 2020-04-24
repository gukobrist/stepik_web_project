# Generated by Django 2.0 on 2020-04-24 14:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20200424_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='question_like_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]