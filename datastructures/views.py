from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required

from .models import Profile, Group, Membership

# Create your views here. 
@login_required
def profile_details_view(request, id = None): 
    student = None
    if id is not None:
        student = Profile.objects.get(id = id)  
    context = {
        "student_obj": student, 
    }
    return render(request, "profiles/profiles-details.html", context = context)

@login_required
def profile_overview_view(request): 
    profile_queryset = Profile.objects.all()
    context = {
        "profile_obj_list": profile_queryset,
    }
    return render(request, "profiles/profiles-overview.html", context = context) 

@login_required
def profile_search_view(request):
    query_dict = request.GET
    query = query_dict.get("query")
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
        user = get_user(request)
        firstName = get_user(request).first_name
        lastName = get_user(request).last_name
        course = request.POST.get("Course")
        studentNumber = request.POST.get("Student Number")
        studyProgram = request.POST.get("Study program")
        gender = request.POST.get("Gender")
        age = request.POST.get("Age")
        course = request.POST.get("Course")
        description = request.POST.get("Description")
        student = Profile.objects.create(user = user, description = description, course = course, firstName = firstName, lastName = lastName, studentNumber = studentNumber, studyProgram = studyProgram, gender = gender, age = age)
        context ['student_obj'] = student 
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
        student_obj.description = request.POST.get("Description")
        student_obj.save()
        return redirect("/")    
    return render (request, "profiles/edit-profile.html", context = context )

@login_required
def groups_overview_view(request):
    groups_queryset = Group.objects.all()
    context = {
        "groups_obj_list" : groups_queryset,
    }
    return render(request, "groups/groups_overview_view.html", context=context)

@login_required
def groups_details_view(request, id):
    group = get_object_or_404(Group, pk=id)
    membership = get_object_or_404(Membership, group = group)
    context = {
        "group_obj": group,
        "membership": membership
    }
    return render(request, "groups/groups_details_view.html", context = context)

@login_required
def groups_delete_view(request, id):
    group = get_object_or_404(Group, pk=id)
    membership = get_object_or_404(Membership, group = group)
    if request.method == "POST":
        if membership.isOwner == True:
            group.delete()
            return redirect("/groups")
        else:
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
        groupDescription = request.POST.get("Description")
        group = Group.objects.create(groupName = groupName, course = course, groupSize = groupSize, groupDescription = groupDescription,)
        current_user = get_user(request)
        profile = get_object_or_404(Profile, user=current_user)
        group_joined = True
        isOwner = True
        owner = Membership.objects.create(profile = profile, group = group, group_joined = group_joined, isOwner = isOwner )
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
            isOwner = False
            membership = Membership.objects.create(profile = profile, group = group, group_joined = group_joined, isOwner = isOwner)
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