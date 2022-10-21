# Generated by Django 3.2.8 on 2022-10-21 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Userprofile', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Businessprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50)),
                ('location', models.CharField(default=None, max_length=300)),
                ('description', models.TextField(default=None, max_length=3000)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('Userprofiles', models.ManyToManyField(blank=True, related_name='businessprofiles', to='Userprofile.Userprofile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businessprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
