from django.urls import path
from .views import Register,Login,Logout,AllTaskTransaction,SingleTaskTransaction

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('all_task_transaction/',AllTaskTransaction.as_view(),name='all_task_transaction'),
    path('single_task_transaction/<int:task_id>',SingleTaskTransaction.as_view(),name='single_task_transaction')

]