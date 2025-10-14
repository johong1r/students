from django.db import models
import datetime

from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):    
    avatar = models.ImageField(verbose_name="Аватарка", upload_to="media")
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст', null=True, blank=True)
    email = models.EmailField(verbose_name='Почта')
    phonenumber = PhoneNumberField(verbose_name='Номер телефона')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа')
    discription = models.TextField(verbose_name="Описание студента")
    join_date = models.DateField(verbose_name="Добавления даты", auto_now_add=True, null=True)
    updated_date = models.DateTimeField(verbose_name="Обновление даты", auto_now_add=True, null=True)
    is_active = models.BooleanField(verbose_name='В присутствие', default=True)
    tags = models.ManyToManyField('Tag', related_name='students', verbose_name='Теги', blank=True)

    def __str__(self):
        return f'{self.name} - {self.id}'
    

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Group(models.Model):
    name = models.CharField()
    updated_date = models.DateTimeField(verbose_name="Обновление даты", auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.id}'
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return f'{self.name} - {self.id}'
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'