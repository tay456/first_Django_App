import csv
from catalog.models import Artists
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print ("Loading CSV")
        csv_path = "./ARTISTS.csv"
        csv_file = open(csv_path, 'rt')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:

            obj = Artists.objects.create(
                id=row['id'],
                brand_name=row['Band Name'],
                manager=row['Manager'],
                contact_number=row['Contact Number'],
                contact_email=row['Contact Email'],
                country=row['Country']
            )
            print (obj)

