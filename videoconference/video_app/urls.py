from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.videocall, name='meeting'),
    path('logout/', views.logout_view, name='logout'),
    path('joinroom/', views.joinroom, name='joinroom'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('profile/', views.profile, name='profile'),
]