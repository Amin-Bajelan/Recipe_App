from core.models import User
from rest_framework import serializers


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        models = "User"
        fields = ["id", "email","is_active", "is_staff", "date_joined", "updated_time"]
        

class CraeteUSerSerializer(serializers.ModelSerializer):
    class Meta: 
        models = "User"    
        fileds =  ["email", "password1", "password2"] 


class EditUSerSerilizers(serializers.ModelSerializer):
    class Meta :
        models = "User"
        fields = ["email", "password"]    
        

        