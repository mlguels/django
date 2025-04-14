from django.http import HttpResponse, JsonResponse
from .models import File
from .serializers import FileSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def files(request):
    f = File.objects.all()
    serializer = FileSerializer(f, many=True)
    return JsonResponse({'files': serializer.data})

def home(request):
    return HttpResponse("Hello there")

@api_view(['GET'])
def file(request, file_id, format=None):
    try:
        f = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FileSerializer(f)
    return JsonResponse({'file': serializer.data})