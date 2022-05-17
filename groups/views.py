from urllib import request
from django.shortcuts import render

from .models import Groups
# Create your views here.

def groups_overview_view(request, gid = None):
    group = None
    return render(request)