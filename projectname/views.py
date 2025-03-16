from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Home page!')

data = [
    {'id': 0, 'name': 'image1.jpeg', 'type': 'jpeg'},
    {'id': 1, 'name': 'notes.txt', 'type': 'txt'},
    {'id': 2, 'name': 'image2.jpeg', 'type': 'jpeg'}
]

def files(request):
    return render(request, 'files/files.html', {'files': data})