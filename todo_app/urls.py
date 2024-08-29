from django.urls import path
from .import views

urlpatterns = [
    path('task/',views.task_list,name='task_list'),
    path('task/<int:pk>/',views.task_details,name='task_details'),
    path('task/add/',views.add_task,name='add_task'),
    path('task/delete/<int:pk>/',views.delete_task,name='delete_task'),
    path('task/update/', views.update_task,name='update_task'),
    path('task/form/', views.add_form, name='task_form')
    
]
