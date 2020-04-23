from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signout/', views.SignoutView.as_view(), name='signout'),
    path('userCreate', views.UserCreateView.as_view(), name='userCreate'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name='index'),
]
