from django.shortcuts import render

from .models import Profile

# Create your views here.

def profile_page_view(request, id = None, *args, **kwargs): 
    student = None
    if id is not None:
        student = Profile.objects.get(id = id) 
    context = {
        "student_obj": student, 
    }

    return render(request, "profiles/profiles.html", context = context)
