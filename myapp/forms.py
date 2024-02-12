from django import forms


class RecipeForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Описание')
    cooking_steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Шаги приготовления')
    cooking_time = forms.FloatField(label='Время приготовления')
    image = forms.ImageField(required=True, label='Изображение')


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

class PKForm(forms.Form):
    pk = forms.IntegerField(min_value=1, label='Введите ')