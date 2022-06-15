"""This file coordinates with new lookup.urls file we created for the VS. The
    import include was added as well as a path call for all urls that are added
    to the VS or found in lookup.urls
"""
from django.contrib import admin
from django.urls import path, include #added new import here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lookup.urls'))   #added new path call here
]


#Now we can basically forget this file. All app additions to the virtual server
#will be primarily delegated through the lookup.urls.py file