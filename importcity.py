import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

import csv
from mysite.models import Country, City

with open("city.csv", "r") as fp:
	rows = csv.DictReader(fp)
	for row in rows:
		name = row["name"]
		country_id = row["country_id"]
		try:
			country = Country.objects.get(id=country_id)
			country_name = country.name
		except:
			country_name = "沒這個國家"
		population = row["population"]
		print("{} : {} : {}".format(country_name, name, population.replace(",", "")))
		c = City(name=name, country=country, population=int(population.replace(",","")))
		c.save()
print("Done~~")
