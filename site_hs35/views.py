from django.shortcuts import render
from .forms import AnketeForm

# Create your views here.


def home_page(request):
    form = AnketeForm()
    return render(request, 'index.html', {'form': form})

def for_pupils(request):
    return render(request, 'pupils.html')

def for_teachers(request):
    return render(request, 'teachers.html')

def for_parents(request):
    return render(request, 'parents.html')