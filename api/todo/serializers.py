from rest_framework import serializers

from .models import List, Task


class ListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='list-detail', read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = List
        fields = ('url', 'id', 'user', 'name')


class TaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail', read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ('url', 'id', 'user', 'list', 'name', 'notes', 'due_date', 'due_time', 'done')
