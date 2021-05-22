# Generated by Django 3.0.5 on 2021-05-22 11:21

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=255)),
                ('post_description', models.TextField()),
                ('comment', djongo.models.fields.JSONField()),
                ('tags', djongo.models.fields.JSONField()),
                ('user_details', djongo.models.fields.JSONField()),
            ],
        ),
    ]
