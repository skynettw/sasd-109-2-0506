import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country

with open("country.csv", "r", encoding="utf-8") as fp:
	data = fp.readlines()
for item in data:
	name = item.split(",")[1].strip()
	print(name)
	c = Country(name=name)
	c.save()
print("Done~~")