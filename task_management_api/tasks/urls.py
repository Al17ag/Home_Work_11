from django.urls import path # path` — это функция, которая позволяет вам создавать маршруты для вашего приложения
from .views import TaskCreateView, TaskListView, TaskStatsView

urlpatterns = [
    path('tasks/', TaskCreateView.as_view(), name='task-create'),
    path('list/', TaskListView.as_view(), name='task-list'),
    path('stats/', TaskStatsView.as_view(), name='task-stats'),
]
