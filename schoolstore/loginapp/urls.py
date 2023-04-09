
from . import views
from django.urls import path
app_name='loginapp'
urlpatterns = [

    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('loggedin',views.loggedin,name='loggedin'),


]
