# Generated by Django 3.2.9 on 2021-12-14 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_designform_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='designform',
            options={'verbose_name': 'Заявки', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelTable(
            name='designform',
            table='Заявки',
        ),
    ]
