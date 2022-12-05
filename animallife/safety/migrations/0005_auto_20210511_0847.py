# Generated by Django 3.1.7 on 2021-05-10 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety', '0004_auto_20210511_0829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='timestamp',
            new_name='begin_timestamp',
        ),
        migrations.AddField(
            model_name='videos',
            name='end_timestamp',
            field=models.CharField(default=0, max_length=305),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='animalusers',
            table=None,
        ),
    ]