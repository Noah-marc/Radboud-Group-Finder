from django.shortcuts import render

from .models import Profile

# Create your views here.

def profile_details_view(request, id = None, *args, **kwargs): 
    student = None
    if id is not None:
        student = Profile.objects.get(id = id) 
    context = {
        "student_obj": student, 
    }

    return render(request, "profiles/profiles-details.html", context = context)

def profile_overview_view(request, *args, **kwargs):
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