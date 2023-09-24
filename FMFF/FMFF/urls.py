"""
URL configuration for FMFF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#this is urls.py in myproject folder
from django.contrib import admin
from django.urls import path, include, re_path
from FindMyFurryFriend import views
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('FindMyFurryFriend/', include('FindMyFurryFriend.urls', namespace='FindMyFurryFriend')),
    path('accounts/', include('accounts.urls')), 
    #path('lost-pets/', views.lost_pet_list, name='lost_pet_list'),
   path('findmyfurryfriend/', views.lost_pet_list, name='lost_pet_list'),
    path('add-lost-pet/', views.add_lost_pet, name='add_lost_pet'),
    path('lost-pet/<int:pet_id>/', views.lost_pet_detail, name='lost_pet_detail'),
     # Define a URL pattern for the root URL ("/") that redirects to the lost pets list
    path('', RedirectView.as_view(pattern_name='lost_pet_list', permanent=False)),
    path('emergency-contacts/list/', TemplateView.as_view(template_name='FindMyFurryFriend/list.html'), name='emergency_contacts_list'),
]

