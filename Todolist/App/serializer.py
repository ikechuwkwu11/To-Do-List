from rest_framework import serializers
from .models import User,Task

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','password']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Task
        fields = '__all__'