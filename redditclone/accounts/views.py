from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            #  Try and find a user with given username, if not, create the new user
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': "User name has already been taken"})

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')

        else:
            return render(request, 'accounts/signup.html', {'error': "Passwords Didn't Match"})

    else:  # GET
        return render(request, 'accounts/signup.html')

def loginView(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            if 'next' in request.POST:                
                return redirect(request.POST['next'])

        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html', {'error': "The Username and Password did not match."})

    else:  # GET
        return render(request, 'accounts/login.html')
