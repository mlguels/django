from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Home page!')

data = [
    {'name': 'image1.jpeg', 'type': 'jpeg'},
    {'name': 'notes.txt', 'type': 'txt'},
    {'name': 'image2.jpeg', 'type': 'jpeg'}
]
def files(request):
    return render(request, 'files/files.html', {'files': data})