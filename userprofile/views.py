from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Userprofile

def signup(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)


            return redirect('/log-in/')
        
    else:    
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form' : form
    })

def logout_view(request):
    """
    Logs the user out (clears their session) and redirects to login.
    """
    logout(request)
    return redirect(reverse('login'))  # or wherever your login URL is named
