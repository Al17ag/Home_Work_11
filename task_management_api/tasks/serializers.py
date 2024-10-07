from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # Преобразует объекты модели `Task` в JSON-формат, который можно отправить клиенту
    class Meta:
        model = Task # Установка модели**: Здесь мы указываем, что сериализатор будет связан с моделью `Task`. Это позволяет сериализатору знать, какие поля и методы доступны для использования.
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at', 'updated_at'] # Указание полей**: Мы определяем список полей, которые будут включены в сериализованное представление
