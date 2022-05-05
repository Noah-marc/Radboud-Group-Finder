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