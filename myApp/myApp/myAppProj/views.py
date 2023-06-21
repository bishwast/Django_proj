from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is awesome'
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'You can rely on our experts'
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to use'
    feature3.details = 'You will find our services very easy to follow and use'
    
    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.details = 'We have affordable prices for our services'
    
    return render(request, 'index.html', {'feature1': feature1, 
                                          'feature2': feature2, 
                                          'feature3': feature3, 
                                          'feature4': feature4})  

def counter(request):
    text = request.POST['text']  ## stores user input from index.html to text variable.
    amountofWords = len(text.split())   ## Splits each unspaced combination of letters to words and counts them.
    return render(request, 'counter.html', {'amount': amountofWords})   # custom key "amount" that stores the count of all words.