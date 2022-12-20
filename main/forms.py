from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, FileExtensionValidator
from .models import User, DesignForm
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    use_required_attribute=False
    username = forms.CharField(label='Логин')
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    fio = forms.CharField(required=True, label='ФИО', max_length=50, validators=[RegexValidator('([А-ЯЁ][а-яё]+[\-\s]?){3,}')])
    person_data = forms.BooleanField(label='Согласие на обработку персональных данных')

    class Meta:
        model = User
        fields = ['fio', 'username', 'password1', 'password2', 'email', 'person_data']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None


class CreateForm(forms.ModelForm):
    use_required_attribute=False
    title = forms.CharField(label='Название', max_length=50, validators=[RegexValidator(regex='[А-ЯЁа-яё]', message='Введите название кириллицей',), ])
    image = forms.ImageField(label='Изображение',validators=[FileExtensionValidator(['png'])])

    class Meta:
        model = DesignForm
        fields = ['title', 'descript', 'category', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Картинка  весит более 1МБ")
            return image
        else:
            raise ValidationError("Картинка не может быть загружена")


class DFAdminForm(forms.ModelForm):
    def clean(self):
        status = self.cleaned_data['status']
        imagecanc = self.cleaned_data['imagecanc']
        if(self.instance.status != status) and status == '1':
            raise ValidationError('Вы не можете поменять статус на Новая!')
        if (self.instance.status == '3'):
            raise ValidationError('Вы не можете поменять статус')
        if (self.instance.status == '2'):
            if (status == '4') and (imagecanc is None):
                raise ValidationError('Добавьте изображение для отмены')
            if (status != '4'):
                raise ValidationError('Вы не можете поменять статус')
        if (status == '4') and (imagecanc is None):
            raise ValidationError('Добавьте изображение для отмены')