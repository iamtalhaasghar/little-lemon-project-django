# Generated by Django 4.2 on 2023-04-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_remove_menuitem_id_menuitem_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='item_id',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
