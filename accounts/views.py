from datastructures.models import Profile
from datastructures.forms import RegisterUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  login, logout, get_user
from django.contrib.auth.forms import AuthenticationForm
from datastructures.forms import RegisterUserForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST": 
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid(): 
            user = form.get_user()
            login(request, user)
            request.session['user_id'] = get_user(request).id
            try:
                current_user = get_user(request)
                get_object_or_404(Profile, user=current_user)
            except:
                return redirect("/profiles/details/create/")
            return redirect("/")
    else: 
        form = AuthenticationForm(request)
    context = {"form" : form}
    return render (request, "accounts/login.html" , context)


def logout_view(request):
    if request.method == "POST": 
        logout(request)
        return redirect ("/")
    return render (request, "accounts/logout.html", {})


def register_view(request):
    form = RegisterUserForm(request.POST or None)
    if form.is_valid(): 
        user_obj = form.save() 
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context )

@login_required
def edit_user_view(request): 
    context = {}
    if request.method == "POST":
        user = get_user(request)
        user.username = request.POST.get("Username")
        user.first_name = request.POST.get("First Name")
        user.last_name = request.POST.get("Last Name")
        user.save()
    return render(request, "accounts/edit-user.html", context = context) 


