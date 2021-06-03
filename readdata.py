import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import MyList

with open("data.txt", "r", encoding="utf-8") as fp:
	data = fp.readlines()
for item in data:
	list_name = item.strip()+"教學影片清單"
	print(list_name)
	r = MyList(name=list_name)
	r.save()