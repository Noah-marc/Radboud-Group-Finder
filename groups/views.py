from multiprocessing import context
from urllib import request
from django.shortcuts import render

from groups.models import Groups
# Create your views here.
# Search groups, overview of all groups, 
# inspect group details, create groups, manage group
# low prio: deleting group, filter function
# create the templates

def groups_overview_view(request, *args, **kwargs):
    groups_queryset = Groups.objects.all()
    context = {
        "groups_obj_list" : groups_queryset
    }
    return render(request, "", context=context)

def groups_details_view(request, groupId=None, *args, **kwargs):
    group = None
    if groupId is not None:
        group = Groups.objects.get(groupId = groupId)
    context = {
        "group_obj": group,
    }
    return render(request, "", context = context)

def groups_delete_view(request, groupId=None, *args, **kwargs):
    group = None
    if groupId is not None:
        group = Groups.objects.get(groupId = groupId)
        group.delete()
    return render(request, "")

def groups_create_view(request):
    context = {}
    if request.method == "POST":
        groupName = request.POST.get("Group Name")
        groupCourse = request.POST.get("Group Course")
        group = Groups.objects.create(groupName = groupName, groupCourse = groupCourse)
        context ['group_obj'] = group
        context ['created'] = True

    return render(request, "", context=context)
