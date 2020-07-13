from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist)})

def about(request):
    return render(request, 'about.html')
