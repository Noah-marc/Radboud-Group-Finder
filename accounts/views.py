from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 

# maybe use include 
def login_view(request):
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is None: 
            context = {"error": "Invalid username or password"}
            return render (request, "accounts/login.html" , context)
        login(request, user)
        return redirect("/profiles/") #TASK: find out how to redirect to 'profiles/details/<int:id>/'
    return render (request, "accounts/login.html" , {})


def logout_view(request):
    if request.method == "POST": 
        logout(request)
        return redirect ("/")
    return render (request, "accounts/logout.html", {})


def register_view(request):
    
    return render(request, "accounts/register.html", {} )



# Create your views here.
