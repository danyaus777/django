from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS_CHOICES = [
    ('1', 'Новая'),
    ('2', 'Принято в работу'),
    ('3', 'Выполнено'),
    ('4', 'Отмена'),
]


class User(AbstractUser):
    def is_author(self, DesignForm):
        if self.pk == DesignForm.user.pk:
            return True
        return False
    fio = models.CharField(max_length=150, verbose_name='ФИО', )


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    class Meta:
        db_table = "Категории"
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        for db in self.db_set.all():
            db.delete()

        super().delete(*args, **kwargs)


class DesignForm(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    descript = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    image = models.ImageField(upload_to='upload/', verbose_name='Изображение')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель заявки')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=1)
    imagecanc = models.ImageField(upload_to='upload/', verbose_name='Изображение для отмены', blank=True)

    class Meta:
        db_table = "Заявки"
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/profile'


class AddCommentary(models.Model):
    form = models.ForeignKey(DesignForm, on_delete=models.CASCADE, verbose_name='Заявки')
    comment = models.CharField(max_length=150, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'


class AddImage(models.Model):
    form = models.ForeignKey(DesignForm, on_delete=models.CASCADE, verbose_name='Заявки')
    image = models.ImageField(upload_to='upload/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Дополнительные фото'
        verbose_name_plural = 'Дополнительные фото'
