from django.conf.urls import include,url

from .views import HomePageView,PopulationPageView, simple_upload, WastageRatePageView, EPIDosagePageView, county_datasets,point_datasets, constituency_datasets

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name = 'home'),
	url(r'^population/$', PopulationPageView.as_view(), name = 'population'),
	url(r'^wastage-rate/$', WastageRatePageView.as_view(), name = 'wastage_rate'),
	url(r'^wastage-rate-upload/$', simple_upload, name = 'wastage_rate_upload'),
	url(r'^epi-dosage/$', EPIDosagePageView.as_view(), name = 'epi_dosage'),
	url(r'^population/$', PopulationPageView.as_view(), name = 'population'),
	url(r'^county_data/$', county_datasets, name = 'county'),
	url(r'^constituency_data/$', constituency_datasets, name = 'constituency'),
	url(r'^incidence_data/$', point_datasets, name = 'incidences'),


]