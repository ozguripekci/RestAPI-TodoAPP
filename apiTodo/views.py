from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )
    

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

#! Function Based Views

""" @api_view(['GET'])
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
    
@api_view(['GET','PUT', 'DELETE'])
def todoUpdate(request, pk):
    
    querset =  Todo.objects.get(id = pk)
    
    if request.method == "GET":
        serializer = TodoSerializer(querset)
    
        return Response(serializer.data)
        
    elif request.method == "PUT":
        
        serializer = TodoSerializer(instance=querset,  data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "DELETE":
      
        querset.delete()
        return Response("Item Deleted")

@api_view(['DELETE'])
def todoDelete(request, pk):
    querset =  Todo.objects.get(id = pk)
    if request.method == "DELETE":
        querset.delete()
        return Response("Item Deleted") """


#! Class Based Views


class TodoList(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class TodoDetail(APIView):

    def get (self, request,id):
        todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    def put(self, request,id):
        todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(instance=todo, data=serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        data = {
            'message': 'Todo is deleted'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
