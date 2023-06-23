from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

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

def register(request):
    
    if request.method =='POST':
        
        # store the user inputed values in the register.html page in the following variables
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_r = request.POST['password_r']

        if password == password_r:       # Only continue is both the password matches
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already used!")
                return redirect('register')     # Send to urlpatters path of register page
            
            elif User.objects.filter(username = username).exists():
                messages.info(request, "Username is already taken, please try another username.")
                return redirect('register')
            
            else:       # If conditions above are false then in User obj sign up the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
            
        else:
            messages.info(request, "Passord does not match!")   # send user to re-register
            return render('register')
        
    else:
        return render(request, 'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password= password)
        
        if user is not None:    # If user is not in DB
            auth.login(request, user)
            return redirect('/')    # Redirect user to hopemage
        else:
            messages.info(request, "Credentials Invalid!")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)    # Logout user out of the page
    return redirect('/')

def counter(request):
    posts = [1,2,3,4,"John", "Tim", "Kim"]
    return render(request, 'counter.html', {'posts': posts})   # custom key "post" that stores the count of all words.

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
