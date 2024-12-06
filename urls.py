from django.urls import path

from . import views

app_name = 'audit'

urlpatterns = [
    path('login/',views.loginv,name="login"),
    path('logout/',views.logoutv,name="logout"),
    path('register/',views.register,name="register"),
]