from django.http import HttpResponse
from django.shortcuts import render
from resume.models import Job, Personal


def home(request):
    job_list = Job.objects.all()
    personal_list = Personal.objects.all()
    context = {
        'job_list': job_list,
        'personal_list': personal_list,
    }
    return render(request, 'resume/resume.html', context)
