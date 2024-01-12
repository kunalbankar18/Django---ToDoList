from django.urls import path
from .views import home, register, custom_login, task_dashboard,create_task,update_task,delete_task,LogoutView,user_profile

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('dashboard/', task_dashboard, name='task_dashboard'),
    path('create/', create_task, name='create_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('user_profile/', user_profile, name='user_profile'),
    path('logout/',LogoutView,name='logout')
]