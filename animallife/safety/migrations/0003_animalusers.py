# Generated by Django 3.1.7 on 2021-05-10 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety', '0002_auto_20210510_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'animal_users',
                'managed': False,
            },
        ),
    ]
