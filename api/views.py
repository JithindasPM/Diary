from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from api.serializers import *
from api.serializers import *
from api.permission import *
from app.models import *

# Create your views here.

class RegistrationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=RegistrationSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class DiaryView(ModelViewSet):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[UserOnly]
    serializer_class=DiarySeralizer
    queryset=Diary_Model.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


