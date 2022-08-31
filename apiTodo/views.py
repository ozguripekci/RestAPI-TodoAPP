from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )
    

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def todoList(request):
    queryset = Todo.objects.all()
    print(queryset)
    serializer = TodoSerializer(queryset, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def todoListCreate(request):
    if request.method == "GET":
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def todoUpdate(request,pk):
        queryset = Todo.objects.get(id=pk)