from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('register/',views.User_register, name='Userregister'),
    path('login/',views.User_login, name='Userlogin'),
    path('logout/',views.user_logout, name='Userlogout'),
    path('profile/',views.profile, name='Userprofile'),
    path('profile/with_pass',views.PassWord_change, name='Change_with_pass'),
    path('profile/without_pass',views.PassWord_change2, name='change_without'),
]