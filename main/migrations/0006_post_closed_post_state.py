# Generated by Django 4.0.4 on 2022-04-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_reply_options_rename_forftags_post_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.CharField(default='zero', max_length=40),
        ),
    ]