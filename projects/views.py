from django.shortcuts import render
from .models import Project


def index(request):
    projet=Project.objects.all()
    return render(request,'index.html', {'projet':projet})
