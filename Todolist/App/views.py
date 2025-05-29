from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout
from .models import User,Task
from .serializer import RegisterSerializer,LoginSerializer,TaskSerializer
from rest_framework import status

class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have been registered.. Now login!'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    def post(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                return Response({'message':'You have been logged in'},status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Logout(APIView):
    def get(self,request):
        try:
            logout(request)
            return Response({'message':'You have been logged out'})
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddTask(APIView):
    def post(self,request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'This is your task','data':serializer.data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleTask(APIView):
    def get(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'message':'This task id does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AllTask(APIView):
    def get(self,request):
        try:
            task = Task.objects.all()
            serializer= TaskSerializer(task, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditTask(APIView):
    def put(self,request,task_id):
        try:
            task = Task.objects.get(id = task_id)
            serializer = TaskSerializer(task,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your data has been updated','data':serializer.data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Task.DoesNotExist:
            return Response({'message':'This request does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteTask(APIView):
    def delete(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return Response({'message':'Your task has been deleted'},status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'message':'This task does not exist!'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)