from django.shortcuts import render
from django.http import HttpResponse
from .models import entry_mol
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the chemdb index.")
    
def all_entries(request):
    entries = entry_mol.objects.all()
    return render(request, 'all_entries.html', {'entries': entries})