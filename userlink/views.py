from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib import messages

def home(request):        
    return render(request, 'home.html')

def redirectToOriginal(request, shortlink):
    try:
        websiteLink = Link.objects.get(shortlink=shortlink).url
        return HttpResponseRedirect(websiteLink)
    except:
        messages.info(request, 'sorry the page does not exist...', extra_tags='Page Does Not Exist!')
        return redirect('/')