from django.shortcuts import render
from django.http import HttpResponse
from .models import entry_mol
from django.conf import settings
import os
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the chemdb index.")
    
def all_entries(request):
    entries = entry_mol.objects.all()
    return render(request, 'all_entries.html', {'entries': entries})




def sketch_view(request, sketch_name):
    sketch_path = os.path.join(settings.MEDIA_ROOT, 'sketches', sketch_name)
    

    if os.path.exists(sketch_path):
        with open(sketch_path, 'rb') as sketch_file:
            response = HttpResponse(sketch_file.read(), content_type='text/img')
            return response
    else:
        return HttpResponse("Sketch not found", status=404)
    

def display_sketch(request, sketch_name):
    return render(request, 'display_sketch.html', {'sketch_name': sketch_name})

def display_mol(request, mol_name):
    mol_path = os.path.join(settings.MEDIA_ROOT, 'mol_files', mol_name + '.mol')
    if os.path.exists(mol_path):
        with open(mol_path, 'rb') as mol_file:
            mol_content = mol_file.read()
            print(mol_content)
            response = render(request, 'display_mol.html', {'mol_content' : mol_content})
            return response
    else:
        return HttpResponse("Mol not found", status=404)
    


