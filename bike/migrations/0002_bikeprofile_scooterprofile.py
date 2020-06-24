# Generated by Django 2.2 on 2020-06-16 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScooterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scooter_image', models.ImageField(default='default.jpg', upload_to='scooter_pics')),
                ('scooter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.COBScooterName')),
            ],
        ),
        migrations.CreateModel(
            name='BikeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_image', models.ImageField(default='default.jpg', upload_to='scooter_pics')),
                ('bike_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.COBBikesData')),
            ],
        ),
    ]