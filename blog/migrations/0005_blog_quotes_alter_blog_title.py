# Generated by Django 5.1.1 on 2024-09-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogreply_sent_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='quotes',
            field=models.CharField(default='You Have the Power To Change the World!', max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
