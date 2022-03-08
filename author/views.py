from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordC = request.POST['passwordC']
        if password == passwordC:
            user = User.objects.create_user(
                first_name = fname,
                last_name = lname,
                username = username,
                email = email,
                password = password
            )
            user.save()
            return redirect('home')       
        return render (request,'author/signup.html', context={'invalid':True})        
    return render(request,'author/signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            username = username,
            password = password
        )
        if user:
            login(request,user)
            return redirect('home')
        return render(request,'author/login.html', context={'invalid':True})    
    return render(request,'author/login.html')


def signout(request):
    logout(request)
    return redirect('home')

