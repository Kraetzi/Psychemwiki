from django.core.management.base import BaseCommand
from chemdb.models import entry_mol
from django.db.models import Count
import os

class Command(BaseCommand):
    help = "Clean the chem_db database by deleting duplicates, filling data from duplicates if .sketch or .mol is not duplicate."

    def handle(self, *args, **options):
        upload_directory = "mol_files/" 

        # Step 1: Get a list of all files in the upload directory
        all_files = set(os.listdir(upload_directory))

        # Step 2: Get a list of all files associated with entries in the database
        files_in_database = set(entry_mol.objects.values_list('dotmol_mol', flat=True))

        # Step 3: Identify files that are in the upload directory but not associated with any database entry
        files_to_delete = set(all_files) - set(os.path.basename(file) for file in files_in_database)

        # Step 4: Delete the identified files
        for file_to_delete in files_to_delete:
            file_path = os.path.join(upload_directory, file_to_delete)
            os.remove(file_path)
            self.stdout.write(self.style.SUCCESS(f"Deleted file: {file_path}"))

        upload_directory = "sketches/"  

        # Step 1: Get a list of all files in the upload directory
        all_files = set(os.listdir(upload_directory))

        # Step 2: Get a list of all files associated with entries in the database
        files_in_database = set(entry_mol.objects.values_list('dotsketch_mol', flat=True))

        # Step 3: Identify files that are in the upload directory but not associated with any database entry
        files_to_delete = set(all_files) - set(os.path.basename(file) for file in files_in_database)

        # Step 4: Delete the identified files
        for file_to_delete in files_to_delete:
            file_path = os.path.join(upload_directory, file_to_delete)
            os.remove(file_path)
            self.stdout.write(self.style.SUCCESS(f"Deleted file: {file_path}"))

