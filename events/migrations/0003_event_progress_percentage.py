# Generated by Django 2.2.6 on 2019-10-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("events", "0002_event_students")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="progress_percentage",
            field=models.IntegerField(default=0),
            preserve_default=False,
        )
    ]
