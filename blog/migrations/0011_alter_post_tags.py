# Generated by Django 5.2 on 2025-06-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
