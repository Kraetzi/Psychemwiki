from django.core.management.base import BaseCommand, CommandError
from chemdb.models import entry_mol as Mol
import os
from django.core.files import File

class Command(BaseCommand):
    help = "Import .mol files to the django db from a directory on machine"

    def add_arguments(self, parser):
        parser.add_argument("directory_path", nargs="+", type=str)

    """
    def handle(self, *args, **options):
        for poll_id in options["poll_ids"]:
            try:
                poll = Mol.objects.get(pk=poll_id)~/Desktop/Project_chemical_database/data_formula/test_folder
            except Mol.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(
                self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
            )
    """
    def handle(self, directory_path, *args, **optional):
        print(directory_path)
        listToStrLS = ' '.join(map(str, directory_path))
        for filename in os.listdir(listToStrLS):
            if filename.endswith(".mol"):
                mol_file_path = os.path.join(listToStrLS, filename)
                
                # Extracting name and text from the mol file (customize accordingly)
                name_mol = filename.replace(".mol", "")
                with open(mol_file_path, 'r') as mol_file:
                    text_mol = mol_file.read()

                # Creating an entry_mol instance and saving to the database
                entry = Mol(name_mol=name_mol, text_mol=text_mol)

                # Adding the .mol file to the FileField
                with open(mol_file_path, 'rb') as mol_file:
                    entry.dotmol_mol.save(filename, File(mol_file))

                # You can customize this part based on your specific requirements
                entry.dotsketch_mol = None  # Set the sketch image field accordingly

                entry.save()

        self.stdout.write(
            self.style.SUCCESS('Successfully got directory "%s"' % directory_path)
        )


# Replace 'your_django_app' with the actual name of your Django app


"""
if __name__ == "__main__":
    directory_path = "/path/to/mol/files"  # Replace with your actual directory path
    add_mol_files_to_model(directory_path)
"""