# Generated by Django 4.2.7 on 2023-11-12 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="timeStamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
