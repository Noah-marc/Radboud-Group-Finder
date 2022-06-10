from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required

import datetime
from .models import Profile, Group, Membership
from django.contrib.auth.models import User
from .forms import ProfileCreationForm

# Create your views here. bruh
@login_required
def profile_details_view(request, id = None, *args, **kwargs): 
    student = None
    if id is not None:
        student = Profile.objects.get(id = id)  
    context = {
        "student_obj": student, 
    }
    return render(request, "profiles/profiles-details.html", context = context)

@login_required
def profile_overview_view(request, *args, **kwargs): #overview of all existitng profiles
    profile_queryset = Profile.objects.all()
    context = {
        "profile_obj_list": profile_queryset
    }
    return render(request, "profiles/profiles-overview.html", context = context) 

@login_required
def profile_search_view(request):
    query_dict = request.GET # this is a dictionary, although syntactically it does not look like a dict
    query = query_dict.get("query") # <input type = 'text' name ='query'/>
    student= None
    if query is not None:
        student = Profile.objects.get(id = query) 
    context = {
        "student_obj": student,
    }
    return render(request, "profiles/search.html", context=context)

def profile_create_view(request): 
    context = {}
    if request.method == "POST": 
        # user = User.objects.get(request.user_id) # van int -> user
        user = get_user(request)
        firstName = get_user(request).first_name
        lastName = get_user(request).last_name
        studentNumber = request.POST.get("Student Number")
        studyProgram = request.POST.get("Study program")
        gender = request.POST.get("Gender")
        age = request.POST.get("Age")
        student = Profile.objects.create(user = user, firstName = firstName, lastName = lastName, studentNumber = studentNumber, studyProgram = studyProgram, gender = gender, age = age)
        context ['student_obj'] = student #this still leads to bugs because of the if statement: When method is GET student is not assigned
        context ['created'] = True
        return redirect("/")
    return render(request, "create-profile.html", context=context) 

def profile_edit_view(request): 
    context = {}
    if request.method == "POST":
        try:
            current_user = get_user(request)
            get_object_or_404(Profile, user=current_user)
        except:
            return redirect("/profiles/details/create/")
        student_obj = get_object_or_404(Profile, user=current_user) 
        student_obj.studentNumber = request.POST.get("Student Number")
        student_obj.studyProgram = request.POST.get("Study program")
        student_obj.gender = request.POST.get("Gender")
        student_obj.age = request.POST.get("Age")
        student_obj.save()
        # Her eneeds to come the actuall passing of the data. Does  "student_obj = get_object_or_404(Profile, user= current_user)" work, such that it has similar context as "t = TemperatureData.objects.get(id=1)" (in regards to what it does generally)
        return redirect("/")    
    return render (request, "profiles/edit-profile.html", context = context )


# def profile_create_view(request): 
#     form = ProfileCreationForm(request.POST or None) 
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         user = get_user(request)
#         firstName = get_user(request).first_name
#         lastName = get_user(request).last_name
#         if form.is_valid: 
#             student_obj = form.save()
#             context["form"] = ProfileCreationForm()
#         return  redirect("/")
#     return render(request, "create-profile.html", context = context )



@login_required
def groups_overview_view(request, *args, **kwargs):
    groups_queryset = Group.objects.all()
    context = {
        "groups_obj_list" : groups_queryset,
    }
    return render(request, "groups/groups_overview_view.html", context=context)

@login_required
def groups_details_view(request, id, *args, **kwargs):
    group = get_object_or_404(Group, pk=id)
    context = {
        "group_obj": group,
    }
    return render(request, "groups/groups_details_view.html", context = context)

@login_required
def groups_delete_view(request, id):
    group = get_object_or_404(Group, pk=id)
    if request.method == "POST":
        group.delete()
        return redirect("/groups")
    context = {
        "object" : group
    }
    return render(request, "groups/groups_delete_view.html", context = context)

@login_required
def groups_create_view(request):
    context = {}
    if request.method == "POST":
        groupName = request.POST.get("Group Name")
        course = request.POST.get("Group Course")
        groupSize = request.POST.get("Group Size")
        group = Group.objects.create(groupName = groupName, course = course, groupSize = groupSize)
        current_user = get_user(request)
        profile = get_object_or_404(Profile, user=current_user)
        group_joined = True
        owner = Membership.objects.create(profile = profile, group = group, group_joined = group_joined)
        context = {
            "group_obj" : group,
            "owner_obj" : owner,
            "created" : True
        } 
        return redirect("/")
    return render(request, "groups/groups_create_view.html", context=context)

@login_required
def join_view(request, id):
    current_user = get_user(request)
    profile = get_object_or_404(Profile, user=current_user)
    group = get_object_or_404(Group, pk=id)
    if request.method == "GET":
        if can_join(profile,group) == True:
            group_joined = True
            membership = Membership.objects.create(profile = profile, group = group, group_joined = group_joined)
            context = {
                "membership_obj" : membership
            }
            return redirect("/groups/")
        else:
            return redirect("/")
    return render(request, "groups/groups_details_view.html", context=context)

def can_join(profile, group):
    i = 0
    for i in range(len(profile.course)):
        s1 = profile.course[i]
        s2 = group.course
        if s1.eq(s2):
            try:
                get_object_or_404(Membership, profile=profile, group=group, group_joined = True)
            except:
                amountMembers = group.members.count()
                if not(amountMembers + 1 > group.groupSize):
                    return True
    return False