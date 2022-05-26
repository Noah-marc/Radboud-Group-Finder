"""
views.py is for rendering html web pages
"""
from django.http import HttpResponse
from django.template.loader import render_to_string
from datastructures.models import Profile

def home_view(request, *args, **kwargs): 
    """
    Take in a request (Django sends requests by default)"
    Retrun HTML as a response (Chosen by us)
    """
    student = Profile.objects.get(id = 1)
    student_queryset = Profile.objects.all()

    context = {
        "student_obj_list": student_queryset,
        "student_obj": student, 
    }
    #Django template
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)

