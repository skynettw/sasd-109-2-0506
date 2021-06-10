from django.contrib import admin
from mysite.models import TVList, MyList, Country, City

class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'population', 'country')

class TVListAdmin(admin.ModelAdmin):
	list_display = ('title', 'vid', 'mylist')

admin.site.register(TVList, TVListAdmin)
admin.site.register(MyList)
admin.site.register(Country)
admin.site.register(City, CityAdmin)
