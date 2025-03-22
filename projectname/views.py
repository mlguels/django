from django.http import HttpResponse ,Http404
from django.shortcuts import render
from .models import File

def home(request):
    return HttpResponse('Home page!')


def files(request):
    data = File.objects.all()
    return render(request, 'files/files.html', {'files': data})
        
def file(request, file_id):
    f = File.objects.get(pk=file_id)
    if f is not None:
        return render(request, 'files/file.html', {'file': f})
    else:
        raise Http404("File does not exist")