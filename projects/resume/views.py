from django.shortcuts import render
from resume.models import Job, Personal
from django.contrib.auth.models import User


def home(request):
    job_list = Job.objects.all()
    personal_list = Personal.objects.all()
    user = User.objects.get(email='krle@lugons.org')
    context = {
        'job_list': job_list,
        'personal_list': personal_list,
        'user': user,
    }
    return render(request, 'resume/resume.html', context)
