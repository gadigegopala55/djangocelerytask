# Generated by Django 4.0.5 on 2022-06-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_rename_comment_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='phonenumber',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]