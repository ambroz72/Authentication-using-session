from unicodedata import name
from django import views
from django.urls import include, path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('about/',views.about,name='about'),

    path('usercreate/',views.usercreate,name="usercreate"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")

]