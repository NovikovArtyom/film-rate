from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, unique=True, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Email')
    login = models.CharField(max_length=20, unique=True, blank=False, null=False, verbose_name='Логин')
    first_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Фамилия')
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Имя')

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email', 'phone', 'first_name', 'last_name']

    def __str__(self):
        return self.login

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class Director(BaseModel):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Actor(BaseModel):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Film(BaseModel):
    title = models.CharField(max_length=25, unique=True, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    release_year = models.IntegerField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    rating = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)
    actor = models.ManyToManyField(Actor, related_name="films")

    def __str__(self):
        return self.title