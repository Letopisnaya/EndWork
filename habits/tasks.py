import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit():
    habits = Habit.objects.all()
    current_date = datetime.datetime.now()
    for habit in habits:
        if habit.time == current_date:
            tg_chat = habit.user.tg_chat_id
            message = f"Сегодня вы должны выполнить полезную привычку {habit.action} в {habit.time} в {habit.place}."
            send_telegram_message(tg_chat, message)
