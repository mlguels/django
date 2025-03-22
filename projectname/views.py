from django.http import HttpResponse ,Http404
from django.shortcuts import render
from django.shortcuts import render, redirect
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
    
def edit(request, file_id):
    name = request.POST.get('name')
    file_type = request.POST.get('type')
    f = File.objects.get(pk=file_id)
    print(name, file_type, f)

    if f:
        if name:
            f.name = name
        if file_type:
            f.file_type = file_type
        f.save()
        return redirect(files)
    else:
        return redirect(files)

def delete(request, file_id):
    f = File.objects.get(pk=file_id)   
    if f:
        f.delete()
    return redirect(files)