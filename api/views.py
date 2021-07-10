from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

# Create your views here.

@api_view(['GET'])
def UserList(request):
	user = User.objects.all().order_by('id')
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def UserDetail(request, pk):
	user = User.objects.get(id=pk)
	serializer = UserSerializer(user, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UserCreate(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def UserUpdate(request, pk):
	user = User.objects.get(id=pk)
	serializer = UserSerializer(instance=user, data=request.data)
	
	if serializer.is_valid():
	 	serializer.save()
	
	return Response(serializer.data)

@api_view(['DELETE'])
def UserDelete(request, pk):
	user = User.objects.get(id=pk)
	serializer = UserSerializer(instance=user, data=request.data)
	user.delete()
	
	return Response('Item succsesfully deleted!')