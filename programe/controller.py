from django.urls import path
from .views import signin,signout,signup,Home
app_name='app'
urlpatterns=[
    path('',signup.as_view(),name='signup'),
    path('signin',signin.as_view(),name='signin'),
    path('signout',signout,name='logout'),
    path('home',Home.as_view(),name='home'),
]