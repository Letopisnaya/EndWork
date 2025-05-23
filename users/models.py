from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=35, null=True, blank=True, verbose_name="Номер телефона")
    tg_nick = models.CharField(max_length=50, null=True, blank=True, verbose_name="Ник телеграм")
    avatar = models.ImageField(upload_to="users/avatars", null=True, blank=True, verbose_name="Аватар")
    tg_chat_id = models.CharField(max_length=150, null=True, blank=True, verbose_name="Телеграм чат-id")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
