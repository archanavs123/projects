from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('product/',views.shop,name='product'),
    path('cart/',views.cart,name='cart'),
]