"""
URL configuration for Diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from app.views import Diary_Home_View,Signin_view,Login_View,Diary_view,Logout_View,All_View,Update_Diary_View
from app.views import Read_View,Delete_Diary_View


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Diary_Home_View.as_view(),name='home'),
    path('sign/', Signin_view.as_view(),name='sign'),
    path('log/', Login_View.as_view(),name='log'),
    path('diary/', Diary_view.as_view(),name='diary'),
    path('logout/', Logout_View.as_view(),name='logout'),
    path('all/', All_View.as_view(),name='all'),
    path('update_diary/<int:pk>', Update_Diary_View.as_view(),name='update_diary'),
    path('read/<int:pk>', Read_View.as_view(),name='read'),
    path('delete/<int:pk>', Delete_Diary_View.as_view(),name='delete'),
    path('api/',include('api.urls')),
]
