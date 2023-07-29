from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, UserChangeForm)


from .models import User, Questions


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Введите имя пользователя',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Введите пароль',
        }
    )) 

    class Meta:
        model = User
        fields = ('username', 'password',)



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Введите имя пользователя',
        }
    ))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input input-width',
            'placeholder': 'Номер телефона',
            'id': 'phone-number'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-input input-width',
            'placeholder': 'Введите эл. почту',
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Введите пароль',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Подтвердите пароль',
        }
    ))
    checkbox = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'checkbox',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'password1', 'password2']



class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Имя пользователя',
        }
    ))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input input-width',
            'placeholder': 'Номер телефона',
            'id': 'phone-number'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-input input-width',
            'placeholder': 'эл. почта',
        }
    ))
    date_of_birth = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input date-input',
            'placeholder': 'ДЕНЬ/МЕСЯЦ/ГОД',
        }
    ))

    GENDER_CHOICES = (
        ('M', 'Мужчина'),
        ('FM', 'Женщина'),
        ('A', 'Другой'),
    )
    sex = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'date_of_birth', 'sex']


class CartForm(forms.Form):
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL')
    ]
    size = forms.ChoiceField(choices=SIZE_CHOICES, widget=forms.RadioSelect(
    ))
    quantity = forms.IntegerField(min_value=1, max_value=10, widget=forms.NumberInput(
        attrs = {
            "readonly": None,
            'value': '1'
        }
    ))

class QuestionsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Ваше имя',
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Ваш e-mail',
        }
    ))
    Text = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Ваш вопрос',
        }
    ))

    class Meta:
        model = Questions
        fields = ['name', 'email', 'Text']