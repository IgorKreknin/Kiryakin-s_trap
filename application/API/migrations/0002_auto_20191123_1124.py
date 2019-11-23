# Generated by Django 2.2.7 on 2019-11-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotIsVisible', models.BooleanField(default=False)),
                ('globalId', models.IntegerField(default=0)),
                ('name', models.TextField()),
                ('district', models.TextField()),
                ('address', models.TextField()),
                ('ovdAddress', models.TextField()),
                ('admArea', models.TextField()),
                ('coordinates', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='parkingslot',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='parkingslot',
            old_name='deparmentalAffilation',
            new_name='departamentalAffilation',
        ),
    ]