"""librarymgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from adminPanel import views


urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('',views.basicwork,name="index"),
    path('home',views.Home.as_view(), name="home"),
    path('signup',views.Register.as_view(), name="signup"),
    path('login',views.Login.as_view(), name="login"),
    path('logout',views.Logout.as_view(), name="logout"),
    path('addbook',views.AddBook.as_view(), name="addbook"),
    path('showbook/<str:bId>',views.ShowBook.as_view(), name="showbook"),




    path('admin/', admin.site.urls),
]
