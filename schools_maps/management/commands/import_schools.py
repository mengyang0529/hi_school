# schools_maps/management/commands/import_schools.py
import os
import json
import numpy as np
from django.core.management.base import BaseCommand
from schools_maps.models import School
from django.db import models

class Command(BaseCommand):
    help = 'Load schools data from JSON file'
    FILE_PATH = './data_analysis/geo_schools.json'  # Constant for file path
    def handle(self, *args, **kwargs):
        try:
            self.load_schools_data()
            self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {self.FILE_PATH}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))

    def load_schools_data(self):
        with open(self.FILE_PATH, 'r') as file:
            data = json.load(file)
            schools_to_create = self.create_school_instances(data)
            School.objects.bulk_create(schools_to_create)

    def create_school_instances(self, data):
        schools = []
        for item in data:
            properties = item['properties']
            location = item['geometry']
            deviation_values = np.array(properties.get('deviation_values', []), dtype=int)

            school = School(
                name=properties['official_name'],
                category=properties['public_or_private'],
                deviation=deviation_values.mean() if deviation_values.size > 0 else 0,
                address=properties['address'],
                region=properties['region'],
                latitude=location['coordinates'][1],
                longitude=location['coordinates'][0],
                url=properties['official_website']
            )
            schools.append(school)
        return schools
