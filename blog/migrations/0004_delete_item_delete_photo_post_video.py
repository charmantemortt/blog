# Generated by Django 5.1.2 on 2024-11-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(null=True, upload_to='videos_uploaded'),
        ),
    ]
