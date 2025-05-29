from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout
from .serializer import RegisterSerializer,LoginSerializer,AccountSerializer,TaskSerializer
from .models import Account
from App.models import Task



class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully registered as an admin... Now login'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    def post(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                return Response({'message':'You have logged in'},status=status.HTTP_200_OK)
            return Response({'message':'Invalid login, please try again'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Logout(APIView):
    def get(self,request):
        try:
            logout(request)
            return Response({'message':'You have been logged out'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AllTaskTransaction(APIView):
    def get(self,request):
        try:
            task = Task.objects.all()
            serializer = TaskSerializer(task,many=True)
            return Response({'message':'This is the whole task','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleTaskTransaction(APIView):
    def get(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task)
            return Response({'message':'This is the task for this client','data':serializer.data},status=status.HTTP_200_OK)
        except Task.DoesMotExist:
            return Response({'message':'This task does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddAccount(APIView):
    def post(self,request):
        try:
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'The account has been created'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AllAccount(APIView):
    def get(self,request):
        try:
            account = Account.objects.all()
            serializer = AccountSerializer(account,many=True)
            return Response({'message':'This are all the accounts that were approved','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)