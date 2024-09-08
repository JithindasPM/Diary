
from django.urls import path
from api.views import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("diary",DiaryView,basename='diary')


urlpatterns = [

    path('registration/',RegistrationView.as_view(),name='registration'),
    path('token/',ObtainAuthToken.as_view(),name='token'),

]+router.urls