# Generated by Django 3.2.8 on 2021-10-28 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Businessprofile', '0002_businessprofile_userprofiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businessprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
