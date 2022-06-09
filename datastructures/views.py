from django.shortcuts import render, get_object_or_404, redirect
import datetime
from .models import Profile, Group, Membership
from django.contrib.auth.models import User

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
        user = request.user
        # firstName = request.user.first_name
        # lastName = request.user.last_name
        firstName = request.POST.get("First Name")
        lastName = request.POST.get("Last Name")
        studentNumber = request.POST.get("Student Number")
        studyProgram = request.POST.get("Study program")
        gender = request.POST.get("Gender")
        age = request.POST.get("Age")
        student = Profile.objects.create(user = user, firstName = firstName, lastName = lastName, studentNumber = studentNumber, studyProgram = studyProgram, gender = gender, age = age)
        context ['student_obj'] = student #this still leads to bugs because of the if statement: When method is GET student is not assigned
        context ['created'] = True
        return redirect("/")
    return render(request, "create-profile.html", context=context) 

def test(request):
    groups_queryset = Group.objects.all()
    context = {
        "groups_obj_list" : groups_queryset,
    }
    return render(request, "test.html", context=context)

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
        return redirect("/groups")
    context = {
        "object" : group
    }
    return render(request, "groups/groups_delete_view.html", context = context)

def groups_create_view(request):
    context = {}
    if request.method == "POST":
        groupName = request.POST.get("Group Name")
        course = request.POST.get("Group Course")
        groupSize = request.POST.get("Group Size")
        group = Group.objects.create(groupName = groupName, course = course, groupSize = groupSize)
        Profile.user = request.user
        profile = get_object_or_404(Profile, pk=Profile.user.id)
        group_joined = True
        owner = Membership.objects.create(profile = profile, group = group, group_joined = group_joined)
        context = {
            "group_obj" : group,
            "owner_obj" : profile,
            "created" : True
        } 
        return redirect("/")
    return render(request, "groups/groups_create_view.html", context=context)

def join_view(request, id, gid):
    profile = get_object_or_404(Profile, pk=id)
    group = get_object_or_404(Group, pk=gid)
    if request.method == "POST":
       if profile.studyProgram == group.groupCourse:
          date_joined = datetime.date.today
          group_joined = True
          membership = Membership.objects.create(profile = profile, group = group, date_joined = date_joined, group_joined = group_joined)
          context = {
              "membership_obj" : membership
          }
    return render(request, "", context=context)


