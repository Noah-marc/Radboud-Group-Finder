"""
views.py is for rendering html web pages
"""
import profile
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from datastructures.models import Membership, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

@login_required
def home_view(request): 
    """
    Take in a request (Django sends requests by default)"
    Retrun HTML as a response (Chosen by us)
    """
    current_user = get_user(request)
    profile = get_object_or_404(Profile, user=current_user)
    membership_queryset = Membership.objects.filter(profile = profile)

    context = {
        "membership_obj_list": membership_queryset,
        "profile_obj": profile,
        "user": current_user
    }
    #Django template
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)

