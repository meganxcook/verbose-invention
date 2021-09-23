# Generated by Django 3.2.7 on 2021-09-23 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_item', models.BooleanField(default=True)),
                ('owned_item', models.BooleanField(default=False)),
                ('image_id', models.CharField(max_length=30)),
                ('image_alt_description', models.TextField()),
                ('image_url', models.URLField()),
                ('thumb_url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
