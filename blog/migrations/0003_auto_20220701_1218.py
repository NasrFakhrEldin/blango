# Generated by Django 3.2.13 on 2022-07-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
