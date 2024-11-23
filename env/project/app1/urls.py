from django.urls import path
from . import views

urlpatterns =[
    path("addTask/", views.addTask, name="add_task"),
    path("",views.taskList,name='task_list'),
    path("diplayTL/",views.display_tasks,name="displayTL"),
    path('task/',views.display_tasks,name='display_tasks'),
    path('tasks/complete/<int:task_id>/', views.complete_Task, name='complete_task'),
    path('tasks/reset/<int:task_id>/',views.reset_task,name ='reset_task'),
    path('task/delTask/<int:task_id>',views.delTask,name ="delTask")
]


