from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request,"myapp/index.html")


def signup(request):
    
    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already exist Please use another username")
                return redirect('/')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email Already exists please use another email')
                return redirect('/')
            else:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save();
                messages.info(request,"Your Account has been Successfully Created.")

                return redirect('signin')
    else:
        return render(request,"myapp/signup.html")

def signin(request):

    if request.method =="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,"myapp/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')
    

    return render(request,"myapp/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"logged Out Successfully!")
    return redirect('home')

    