from django.shortcuts import render
from .models import superProfile
from markdown import markdown

# Create your views here.
def about(request):
    aboutlist = superProfile.objects.get()
    return render(request, 'about/about.html', context={'aboutlist': aboutlist})