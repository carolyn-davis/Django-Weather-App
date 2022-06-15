#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:32:54 2022

@author: carolyndavis
"""

# =============================================================================
# THIS IS THE URL.PY IN THE LOOKUP DIRECTORY
# =============================================================================

"""In a URL Framework you need three things...
    1.) URL - something to point the thing to (an actual one page)
    2.) HTML page - template
    3.) View.py/View file--- allow us to use python in our app """

from django.urls import path

from . import views  #from this directory import views

"""This function creates a url. The path for the url is nothing. It points to views.home  """

urlpatterns = [
    path('', views.home, name="home"), #this path is left blank bc its the homepage, all others will have nme
    path('about.html', views.about, name="about")
]
