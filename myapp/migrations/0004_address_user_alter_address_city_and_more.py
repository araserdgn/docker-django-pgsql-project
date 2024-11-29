# Generated by Django 5.1.3 on 2024-11-29 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_address_user_alter_address_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='myapp.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='geo_lat',
            field=models.DecimalField(decimal_places=6, max_digits=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='geo_lng',
            field=models.DecimalField(decimal_places=6, max_digits=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='suite',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='myapp.user'),
        ),
    ]