from rest_framework.serializers import ValidationError


class HabitValidators:
    def __call__(self, value):
        val = dict(value)
        if val.get("related_habit") and val.get("reward"):
            raise ValidationError("Нельзя совмещать приятную привычку и вознаграждение")

        if val.get("time_complete") > 120:
            raise ValidationError("Время на выполнение не должно превышать 120 секунд")

        habit = val.get("related_habit")
        if habit:
            if not habit.nice_habit:
                raise ValidationError("Связанная привычка должна быть приятной")

        if val.get("nice_habit") is True and val.get("reward"):
            raise ValidationError("У приятной привычки не должно быть вознаграждения")

        if val.get("nice_habit") is True and val.get("related_habit"):
            raise ValidationError("У приятной привычки не должно быть связанной привычки")

        if val.get("periodicity") < 1 or val.get("periodicity") > 7:
            raise ValidationError("Периодичность выполнения должна быть не менее 1 раз в 7 дней")
