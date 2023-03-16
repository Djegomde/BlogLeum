# Generated by Django 4.1.7 on 2023-03-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo_profil',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='author',
            name='telephone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='commentaire',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_post',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]