from django.urls import path

from user_profile_app import views

urlpatterns = [
    path('login/', views.login_user,name='login'),
    path('register/', views.register_user,name='register_user'),
    path('login/', views.login_user,name='login_user'),
    path('logout/', views.logout_user,name='logout_user'),
    path('profile/', views.profile,name='profile'),
    path('profile/', views.profile,name='profile'),
    path('change_profile_picture/', views.change_profile_picture,name='change_profile_picture'),

]
