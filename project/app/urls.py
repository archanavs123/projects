from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='home'),
    path('loginn/',views.user_login,name='loginn'),
    path('signUp/',views.user_signup,name='signUp'),
    path('logout/',views.user_logout,name='logout1'),
]
