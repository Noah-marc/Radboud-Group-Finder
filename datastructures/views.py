<<<<<<< HEAD:profiles/views.py
from pickle import NONE
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm

=======
from django.shortcuts import render, get_object_or_404, redirect

from .models import Profile
from .models import Group
from .models import Membership
>>>>>>> cc097d128c3fdaee8a9ef65fe329c34412a595a4:datastructures/views.py

# Create your views here. bruh

def profile_details_view(request, id = None, *args, **kwargs): 
    student = None
    if id is not None:
        student = Profile.objects.get(id = id)  
    context = {
        "student_obj": student, 
    }
    return render(request, "profiles/profiles-details.html", context = context)

def profile_overview_view(request, *args, **kwargs): #overview of all existitng profiles
    profile_queryset = Profile.objects.all()
    context = {
        "profile_obj_list": profile_queryset
    }
    return render(request, "profiles/profiles-overview.html", context = context) 

def profile_search_view(request):
    query_dict = request.GET # this is a dictionary, although syntactically it does not look like a dict
    query = query_dict.get("query") # <input type = 'text' name ='query'/>
    student= None
    if query is not None: #NEEDS TO MODIFIED, catch exceptions when wrong input type, etc. (cf. try-django for the problem)
        student = Profile.objects.get(id = query) 
    context = {
        "student_obj": student,
    }
    return render(request, "profiles/search.html", context=context)

@login_required
def profile_create_view(request): 
    form = ProfileForm()

    context = {
        "form": form
    }
    # clean data
    if request.method == "POST": 
<<<<<<< HEAD:profiles/views.py
        form = ProfileForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data.get("firstName")
            lastName = form.cleaned_data.get("lastName")
            studentNumber = form.cleaned_data.get("studentNumber")
            studyProgram = form.cleaned_data.get("studyProgram")
            gender = form.cleaned_data.get("gender")
            age = form.cleaned_data.get("age")
            student = Profile.objects.create(firstName = firstName, lastName = lastName, studentNumber = studentNumber, studyProgram = studyProgram, gender = gender, age = age)
            context ['student_obj'] = student #this still leads to bugs because of the if statement: When method is GET student is not assigned
            context ['created'] = True
    return render(request, "profiles/create-profile.html", context = context)

# @login_required
# def profile_create_view(request): 
#    form = ProfileForm(request.POST or NONE)
 #   context = {
  #      "form": form
  #  }
   # if form.is_valid(): 
    #    firstName = request.POST.get("firstName")
     #   lastName = request.POST.get("lastName")
      #  studentNumber = request.POST.get("studentNumber")
       # studyProgram = request.POST.get("studyProgram")
    #    gender = request.POST.get("gender")
     #   age = request.POST.get("age")
      #  student = Profile.objects.create(firstName = firstName, lastName = lastName, studentNumber = studentNumber, studyProgram = studyProgram, gender = gender, age = age)
     #   context ['student_obj'] = student #this still leads to bugs because of the if statement: When method is GET student is not assigned
     #   context ['created'] = True
   # return render(request, "profiles/create-profile.html", context = context)
=======
        firstName = request.POST.get("First Name")
        lastName = request.POST.get("Last Name")
        studentNumber = request.POST.get("Student Number")
        studyProgram = request.POST.get("Study program")
        gender = request.POST.get("Gender")
        age = request.POST.get("Age")
        student = Profile.objects.create(firstName = firstName, lastName = lastName, studentNumber = studentNumber, studyProgram = studyProgram, gender = gender, age = age)
        context ['student_obj'] = student #this still leads to bugs because of the if statement: When method is GET student is not assigned
        context ['created'] = True
    return render(request, "create-profile.html", context=context) 

def test(request):
    groups_queryset = Group.objects.all()
    context = {
        "groups_obj_list" : groups_queryset,
    }
    return render(request, "test.html", context=context)

def sidebar_view(request):
    context = {}
    return render(request, "sidebar-test.html", context=context)
    
def groups_overview_view(request, *args, **kwargs):
    groups_queryset = Group.objects.all()
    context = {
        "groups_obj_list" : groups_queryset,
    }
    return render(request, "groups/groups_overview_view.html", context=context)

def groups_details_view(request, id, *args, **kwargs):
    group = get_object_or_404(Group, pk=id)
    context = {
        "group_obj": group,
    }
    return render(request, "groups/groups_details_view.html", context = context)

def groups_delete_view(request, id):
    group = get_object_or_404(Group, pk=id)
    if request.method == "POST":
        group.delete()
        print("test")
        return redirect("/groups")
    context = {
        "object" : group
    }
    return render(request, "groups/groups_delete_view.html", context = context)

def groups_create_view(request):
    context = {}
    if request.method == "POST":
        groupName = request.POST.get("Group Name")
        groupCourse = request.POST.get("Group Course")
        group = Group.objects.create(groupName = groupName, groupCourse = groupCourse)
        context ['group_obj'] = group
        context ['created'] = True

    return render(request, "", context=context)
>>>>>>> cc097d128c3fdaee8a9ef65fe329c34412a595a4:datastructures/views.py
