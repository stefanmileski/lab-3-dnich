# Generated by Django 4.2.1 on 2023-05-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_comment_post_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
    ]
