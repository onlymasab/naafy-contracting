# Generated by Django 5.1.1 on 2024-09-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_featured_image_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogreply',
            name='response',
            field=models.BooleanField(default=False),
        ),
    ]
