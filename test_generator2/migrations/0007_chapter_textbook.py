# Generated by Django 5.0.4 on 2024-06-23 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_generator2', '0006_textbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='textbook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_generator2.textbook'),
        ),
    ]
