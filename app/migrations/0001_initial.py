# Generated by Django 4.0.5 on 2022-06-20 11:31

import cloudinary.models
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
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood_name', models.CharField(max_length=100)),
                ('neighborhood_location', models.CharField(max_length=100)),
                ('health_tell', models.BigIntegerField(blank=True, null=True)),
                ('police_number', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=100)),
                ('neighborhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.neighborhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('post', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('description', models.TextField()),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='app.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='app.profile'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
    ]
