# Generated by Django 4.0.4 on 2022-06-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_post_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='region',
            field=models.CharField(choices=[('서울', '서울'), ('수원', '수원'), ('부산', '부산')], max_length=10),
        ),
    ]