from django.contrib import admin
from .models import Incidences, Counties, Constituencies
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('name','location')

class CountiesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('county_nam','county_cod', 'shape_area')

class ConstituenciesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('constituen','county_cod', 'shape_area')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
admin.site.register(Constituencies, ConstituenciesAdmin)
