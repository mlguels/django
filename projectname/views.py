from django.http import HttpResponse, JsonResponse
from .models import File
from .serializers import FileSerializer
from .serializers import FileSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def files(request, format=None):
    if request.method == 'GET':
        data = File.objects.all()
        serializer = FileSerializer(data, many=True)
        return Response({'files': serializer.data})
    
    elif request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return HttpResponse("Hello there")

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def file(request, file_id, format=None):
    try:
        f = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FileSerializer(f)
        return Response({'file': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        serializer = FileSerializer(f, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        f.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)