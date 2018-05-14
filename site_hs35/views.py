from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'index.html')

def for_pupils(request):
    return render(request, 'pupils.html')

def for_teachers(request):
    return render(request, 'teachers.html')

def for_parents(request):
    return render(request, 'parents.html')