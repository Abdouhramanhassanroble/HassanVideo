from django.urls import path, include
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView
urlpatterns = [
    path('', views.login_view, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.videocall, name='meeting'),
    path('logout/', views.logout_view, name='logout'),
    path('joinroom/', views.joinroom, name='joinroom'),
    path('profile/', views.profile, name='profile'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>/', TaskUpdate.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]