from django.shortcuts import render
from .models import Job
from faker import Faker
import requests
from pprint import pprint
fake = Faker()

URL = 'https://api.giphy.com/v1/gifs/search?api_key=RjZx308jT3k2uLnMk3lgQK4o7sGi4GYt&limit=1&lang=en&q='

def index(request):
    return render(request, 'jobs/index.html')


def past_job(request):

    name = request.POST.get('name')
    if Job.objects.filter(name=name):
        job = Job.objects.get(name=name)
    else:
        job = Job()
        job.name = name
        job.past_job = fake.job()
        job.save()

    url = URL + job.past_job
    data = requests.get(url).json()
    data = data.get('data')[0].get('images').get('downsized').get('url')

    context = {
        'job':job,
        'data':data
        }
        
    return render(request, 'jobs/past_job.html', context)