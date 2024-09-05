from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
# from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer



@login_required
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
       
       
@login_required
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=400)
       
       
          
# class ToDoList(generics.ListCreateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

# class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
   