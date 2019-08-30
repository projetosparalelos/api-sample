from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .serializers import ListSerializer, TaskSerializer


class ListViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all existing to do lists.

    create:
    Create and return a new to do list.

    retrieve:
    Return a single to do list.

    update:
    Update an existing to do list.

    partial_update:
    Update an existing to do list.

    destroy:
    Delete an existing to do list.
    """
    serializer_class = ListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name',)

    def get_queryset(self):
        return self.request.user.list_set.all()


class TaskViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all existing tasks.

    create:
    Create and return a new task.

    retrieve:
    Return a single task.

    update:
    Update an existing task.

    partial_update:
    Update an existing task.

    destroy:
    Delete an existing task.
    """
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('id', 'list', 'done')
    ordering_fields = ('name', 'due_date', 'due_time')
    search_fields = ('name',)

    def get_queryset(self):
        return self.request.user.task_set.all()
