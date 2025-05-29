from rest_framework import serializers
from .models import Admin,Account
from App.models import Task



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields='__all__'

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = Admin
        fields = ['email', 'password']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    what_task = TaskSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'account', 'what_task', 'is_active', 'created_at']