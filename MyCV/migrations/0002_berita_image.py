# Generated by Django 4.2.11 on 2024-03-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='image',
            field=models.ImageField(default='', upload_to='image/'),
        ),
    ]
