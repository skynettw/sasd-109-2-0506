from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import TVList, MyList, Country, City

def charts(request):
	countries = Country.objects.all()
	cities = City.objects.all()

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
