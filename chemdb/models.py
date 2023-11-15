from django.db import models

# Create your models here.

class entry_mol(models.Model):
    name_mol = models.CharField(max_length=200)
    text_mol = models.TextField()
    dotsketch_mol = models.ImageField(upload_to="sketches")
    dotmol_mol = models.FileField(upload_to="mol_files")
