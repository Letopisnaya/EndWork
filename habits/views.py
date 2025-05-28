from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, IsOwner)


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsPublicListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
