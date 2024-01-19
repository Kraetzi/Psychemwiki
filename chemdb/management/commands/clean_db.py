from django.core.management.base import BaseCommand
from chemdb.models import entry_mol
from django.db.models import Count

class Command(BaseCommand):
    help = "Clean the chem_db database by deleting duplicates, filling data from duplicates if .sketch or .mol is not duplicate."

    def handle(self, *args, **options):
        # Identify duplicate entries based on the fields you consider for uniqueness
        duplicate_entries = (
            entry_mol.objects.values('name_mol')  # Adjust fields as needed
            .annotate(count=Count('id'))
            .filter(count__gt=1)
        )

        for duplicate in duplicate_entries:
            # Retrieve all duplicates for a specific combination of fields
            duplicates_to_merge = entry_mol.objects.filter(
                name_mol=duplicate['name_mol'],
            )  # Exclude the first occurrence

            print(f"Merging duplicates for {duplicate['name_mol']}")

            # Merge information - customize this based on your needs
            first_entry = entry_mol.objects.filter(name_mol=duplicate['name_mol']).first()

            for duplicate_entry in duplicates_to_merge:
                # Merge information from duplicate_entry to first_entry
                if not first_entry.text_mol and duplicate_entry.text_mol and duplicate_entry.text_mol != "":
                    first_entry.text_mol = duplicate_entry.text_mol

                if not first_entry.dotsketch_mol and duplicate_entry.dotsketch_mol:
                    first_entry.dotsketch_mol = duplicate_entry.dotsketch_mol

                if not first_entry.dotmol_mol and duplicate_entry.dotmol_mol:
                    first_entry.dotmol_mol = duplicate_entry.dotmol_mol

                # Delete the duplicate entry
                duplicate_entry.delete()

            # Save the updated first_entry
            first_entry.save()
