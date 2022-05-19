from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from cameraapp.forms import Camera_form
from cameraapp.models import Camera


def index(request):
    all_video = Camera.objects.all()
    if request.method == "POST":
        form = Camera_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cameraapp:list')
    else:
        form = Camera_form()
    return render(request, 'cameraapp/index.html', {"form": form, "all": all_video})


def list_index(request):
    all_video = Camera.objects.all()
    if request.method == "POST":
        form = Camera_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cameraapp:list')
    else:
        form = Camera_form()
    return render(request, 'cameraapp/list.html', {"form": form, "all": all_video})