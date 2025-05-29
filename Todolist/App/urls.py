from django.urls import path
from .views import Register,Login,Logout,AddTask,SingleTask,AllTask,EditTask,DeleteTask

urlpatterns= [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('add_task/', AddTask.as_view(),name='add_task'),
    path('single_task/<int:task_id>',SingleTask.as_view(),name='single_task'),
    path('all_task/',AllTask.as_view(),name='all_task'),
    path('edit_task/<int:task_id>',EditTask.as_view(),name='edit_task'),
    path('delete_task/<int:task_id>',DeleteTask.as_view(),name='delete_task')

]