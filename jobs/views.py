from django.shortcuts import render

from .models import Job

# Create your views here.
def home(request):
    Jobs = Job.objects
    return render(request, 'jobs/home.html', {"Jobs":Jobs})
