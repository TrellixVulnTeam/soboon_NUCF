# Generated by Django 2.1.3 on 2019-06-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_content2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
