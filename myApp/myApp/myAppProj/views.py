from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
##def index(request): 
"""  feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is awesome'
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'You can rely on our experts'
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to use'
    feature3.is_true = False
    feature3.details = 'You will find our services very easy to follow and use'
    
    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.is_true = True
    feature4.details = 'We have affordable prices for our services'
    
    features = [feature1, feature2, feature3, feature4]
    
    return render(request, 'index.html', {'features': features})  
    
    SELF-NOTE: Since I created a model, migrated the database and created admin account in admin panel, I do 
    not need these features anymore. As I can add features to the Feature() class from the admin panel.
    """
    
def index(request):
    features = Feature.objects.all()    # grab all objects from Feature() database and store in features variable.
    return render(request, 'index.html', {'features': features})

def counter(request):
    text = request.POST['text']  ## stores user input from index.html to text variable.
    amountofWords = len(text.split())   ## Splits each unspaced combination of letters to words and counts them.
    return render(request, 'counter.html', {'amount': amountofWords})   # custom key "amount" that stores the count of all words.