# Generated by Django 3.2.9 on 2022-03-21 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0002_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
