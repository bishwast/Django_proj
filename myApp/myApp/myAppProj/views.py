from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Jon',
        'age': 22,
        'country': 'USA',
        'city': 'Salt Lake City'
    }
    return render(request, 'index.html', context)   # Context will be sent to index.html in templates folder