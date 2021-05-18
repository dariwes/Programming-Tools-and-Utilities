# Generated by Django 3.2 on 2021-05-18 10:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
