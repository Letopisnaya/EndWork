from django.db import models

from config import settings


class Habit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
    )
    place = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Место выполнения привычки",
    )
    time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Время выполнения привычки",
    )
    action = models.CharField(max_length=250, verbose_name="Действие")
    nice_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
    )
    periodicity = models.PositiveIntegerField(default=1, verbose_name="Периодичность")
    reward = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Вознаграждение",
    )
    time_complete = models.PositiveIntegerField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.action
