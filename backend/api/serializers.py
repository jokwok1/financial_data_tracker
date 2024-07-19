from django.contrib.auth.models import User
from .models import Entry

from rest_framework import serializers 

class UserSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = User 
        fields = ["id", "username", "password"] 
        extra_kwargs = {"password" : {"write_only" : True}}  
     
    # Method to create user 
    def create(self, validated_data):  
        user = User.objects.create_user(**validated_data) 
        return user 


class EntrySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Entry 
        fields = ["id", "category", "amount", "date", "author"]
        extra_kwargs = {"author": {"read_only": True}}


