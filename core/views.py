from django.shortcuts import render
from .models import Patient

# Create your views here.


def index(request):
    datas=Patient.objects.all()
    return render(request, 'index.html', {'datas':datas})
