from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SEX_CHOICES = [
        ('M', 'Мужчина'),
        ('FM', 'Женщина'),
        ('A', 'Другой'),
    ]
    phone_number = models.CharField(max_length=19)
    date_of_birth = models.CharField(max_length=10, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True, blank=True)


    def __str__(self):
        return self.username
    

class Questions(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    email = models.EmailField(max_length=128, verbose_name='Почта')
    Text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'Questions'
    