# Generated by Django 3.2.25 on 2025-05-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_delete_chatpair'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
