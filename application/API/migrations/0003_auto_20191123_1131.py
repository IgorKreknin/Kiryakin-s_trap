# Generated by Django 2.2.7 on 2019-11-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20191123_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='coordinates',
            field=models.TextField(),
        ),
    ]