# Generated by Django 4.2.2 on 2023-07-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0002_alter_authuser_age_alter_authuser_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
