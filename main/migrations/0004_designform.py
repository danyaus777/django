# Generated by Django 3.2.9 on 2021-12-11 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211212_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('descript', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='upload/', verbose_name='Изображение')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('1', 'Новая'), ('2', 'Принято в работу'), ('3', 'Выполнено')], default=1, max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель заявки')),
            ],
        ),
    ]