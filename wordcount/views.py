from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):   # request: is there this url we need?
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('<h1>eggs are great</h1>')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sorted_words = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'sorted_words':sorted_words})

def about(request):
    return render(request, 'about.html')
