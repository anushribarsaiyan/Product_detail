import csv
import json
from django.core.management.base import BaseCommand
from app.models import AllProducts
from app.models import AllProducts, RelaxedFit, RegularFit

class Command(BaseCommand):
    help = 'Populate data from CSV file to database'

    def handle(self, *args, **options):
        file_path = 'C:/Users/Asus/Desktop/home/project/app/flipkart.csv'

        # Open the CSV file and create a CSV reader
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)

            # Iterate through rows and create or update model instances
            for row in reader:
                # Convert 'is_FK_Advantage_product' to boolean
                row['is_FK_Advantage_product'] = row.get('is_FK_Advantage_product', '').lower() == 'true'

                try:
                    # Convert the 'retail_price' value to a float
                    retail_price = float(row.get('retail_price', '').strip())
                    # Convert the 'discounted_price' value to a float
                    discounted_price = float(row.get('discounted_price', '').strip())

                    # Remove 'retail_price' and 'discounted_price' from the row dictionary
                    row.pop('retail_price', None)
                    row.pop('discounted_price', None)

                    # Check if a record with the same uniq_id exists
                    obj, created = AllProducts.objects.update_or_create(
                        uniq_id=row['uniq_id'],
                        defaults={
                            'retail_price': retail_price,
                            '    ': discounted_price,
                            **row
                        }
                    )

                    if not created:
                        self.stdout.write(self.style.SUCCESS(f"Record with uniq_id={row['uniq_id']} updated successfully."))

                except ValueError:
                    self.stdout.write(self.style.ERROR(f"Invalid price value for row with uniq_id={row.get('uniq_id', '')}"))

        self.stdout.write(self.style.SUCCESS('Data populated successfully.'))





