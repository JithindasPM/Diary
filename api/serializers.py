from rest_framework import serializers
from app.models import User,Diary_Model



class DiarySeralizer(serializers.ModelSerializer):
    class Meta:
        model=Diary_Model
        fields="__all__"
        read_only_field=['id','created_date','user']


class RegistrationSeralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=fields=['id','username','first_name','last_name','email','password']
        read_only_field=['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

