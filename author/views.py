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



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            username = username,
            password = password
        )
        if user:
            login(request)
        
        print(username,password)
    return render(request,'author/login.html')


def logout(request):
    logout(request)
    return redirect('home')

