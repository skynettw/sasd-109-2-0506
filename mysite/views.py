from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import TVList, MyList, Country, City

def plist(request, name=""):
	countries = Country.objects.all()
	if request.method == 'POST':
		#這是從表單來的請求
		country_id = request.POST["country"]
		items = int(request.POST["items"])
		target = Country.objects.get(id=country_id)
		if target != None:
			if items == 0:
				cities = City.objects.filter(country=target).order_by("population")
			else:	
				cities = City.objects.filter(country=target).order_by("population")[:items]
		else:
			if items == 0:
				cities = City.objects.all().order_by("-population")
			else:
				cities = City.objects.all().order_by("-population")[:items]
	else:
		#這是從網址來的請求
		if name != "":
			target = Country.objects.get(name=name)
			if target != None:
				cities = City.objects.filter(country=target).order_by("population")
			else:
				cities = City.objects.all().order_by("-population")	
		else:
			cities = City.objects.all().order_by("-population")
	return render(request, "plist.html", locals())	

def charts(request):
	countries = Country.objects.all()
	cities = City.objects.all().order_by("population")
	return render(request, "charts.html", locals())

def index(request):
	names = ["何敏煌", "王小花", "李白", "袁枚"]
	years = range(1960, 2001)
	return render(request, "index.html", locals())

def playlist(request, id=0):
	mylist = MyList.objects.all()
	try:
		target_list = MyList.objects.get(id=id)
	except:
		pass
	if id == 0:
		tvlist = TVList.objects.all()
	else:
		tvlist = TVList.objects.filter(mylist=target_list)
	return render(request, "playlist.html", locals())

def play(request, id=1):
	try:
		target = TVList.objects.get(id=id)
	except:
		target = TVList.objects.get(id=1)
	return render(request, "play.html", locals())

def bmi(request):
	if request.method == "POST":
		height = int(request.POST["height"])
		weight = int(request.POST["weight"])
		bmi = weight / ((height/100) ** 2)
	return render(request, "bmi.html", locals())

def lucky(request):
	lucky = random.randint(1, 99)
	return HttpResponse("本日幸運數字：{}".format(lucky))
