# Generated by Django 4.2.7 on 2023-11-12 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_alter_post_timestamp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="views",
        ),
    ]
