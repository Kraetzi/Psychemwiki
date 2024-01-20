from django.core.management.base import BaseCommand
from chemdb.models import entry_mol

class Command(BaseCommand):
    help = "Delete all entries in the database."

    def handle(self, *args, **options):
        # Delete all entries in the database
        entry_mol.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("All entries have been deleted."))
