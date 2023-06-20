from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')  

def counter(request):
    text = request.POST['text']  ## stores user input from index.html to text variable.
    amountofWords = len(text.split())   ## Splits each unspaced combination of letters to words and counts them.
    return render(request, 'counter.html', {'amount': amountofWords})   # custom key "amount" that stores the count of all words.