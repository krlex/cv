from django.http import HttpResponse
from django.shortcuts import render
from resume.models import Job


def home(request):
    job_list = Job.objects.all()
    context = {"job_list": job_list}
    return render(request, 'resume/resume.html', context)

