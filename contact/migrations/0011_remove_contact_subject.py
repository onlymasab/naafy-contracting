# Generated by Django 5.1.1 on 2024-10-01 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_contactdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
