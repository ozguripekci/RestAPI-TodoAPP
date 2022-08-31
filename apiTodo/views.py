from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer

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
