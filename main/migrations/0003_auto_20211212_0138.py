# Generated by Django 3.2.9 on 2021-12-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_fio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='fio',
            field=models.CharField(max_length=150, verbose_name='ФИО'),
        ),
    ]
