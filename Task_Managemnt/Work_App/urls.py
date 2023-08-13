from django.urls import path

from . views import home, create_task, edit_task, show_task, complete_task, delete_task,completed_task_lists

urlpatterns = [
    path('', home),
    path('show/', show_task, name='showtaskpage'),
    path('create/', create_task, name='createtaskpage'),
    path('edit/<int:id>', edit_task, name='edittaskpage'),
    path('deletetaskpage/<int:id>', delete_task, name='deletetaskpage'),
    path('complete/<int:id>', complete_task, name='completetaskpage'),
    path('completed/', completed_task_lists, name='completedtaskpage'),
]
