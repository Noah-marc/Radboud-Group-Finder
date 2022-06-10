"""RadboudGroupFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import home_view
from datastructures import views

from accounts import views as account_views

urlpatterns = [
    path('', home_view), #home/ root page
    path('profiles/', views.profile_overview_view),
    path('profiles/details/', views.profile_search_view ),
    path('profiles/details/create/', views.profile_create_view),
    path('profiles/details/<int:id>/', views.profile_details_view),
    path('profiles/edit/', views.profile_edit_view),

    path('groups/', views.groups_overview_view),
    path('groups/details/<int:id>/', views.groups_details_view),
    path('groups/details/<int:id>/join', views.join_view),
    path('groups/details/<int:id>/delete/', views.groups_delete_view),
    path('groups/create/', views.groups_create_view),
    
    path('admin/', admin.site.urls),
    path('login/', account_views.login_view), 
    path('logout/', account_views.logout_view),
    path('register/', account_views.register_view),
    path('edit-user/', account_views.edit_user_view), 
]
