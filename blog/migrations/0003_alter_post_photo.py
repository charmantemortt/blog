# Generated by Django 5.1.2 on 2024-11-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_item_photo_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]