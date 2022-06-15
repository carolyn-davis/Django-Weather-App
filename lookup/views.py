from django.shortcuts import render
"""This function points thing to the thing. Step 2 after the creation of the 
    HTML template"""
# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})  #adding new view for about me 