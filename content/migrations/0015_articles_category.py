# Generated by Django 5.1 on 2024-08-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_message_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
