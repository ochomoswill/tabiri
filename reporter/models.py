from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Incidences(models.Model):
	name = models.CharField(max_length=20)
	location = models.PointField(srid=4326)
	objects = models.GeoManager()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural =" Incidences"

""" class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
    	return self.counties

    class Meta:
        verbose_name_plural = 'Counties' """


class Counties(models.Model):
    objectid = models.BigIntegerField(null=True)
    id_field = models.BigIntegerField(null=True)
    county_nam = models.CharField(max_length=80, null=True)
    const_code = models.BigIntegerField(null=True)
    constituen = models.CharField(max_length=80, null=True)
    county_cod = models.BigIntegerField(null=True)
    shape_leng = models.FloatField(null=True)
    shape_area = models.FloatField(null=True)
    geom = models.MultiPolygonField(srid=4326, null=True)

    def __unicode__(self):
    	return self.county_nam

    class Meta:
        verbose_name_plural = 'Counties'


class Constituencies(models.Model):
    objectid = models.BigIntegerField()
    county_nam = models.CharField(max_length=80)
    const_code = models.FloatField()
    constituen = models.CharField(max_length=80)
    county_ass = models.FloatField()
    county_a_1 = models.CharField(max_length=80)
    regist_cen = models.FloatField()
    registrati = models.CharField(max_length=80)
    county_cod = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
    	return self.constituen

    class Meta:
        verbose_name_plural = 'Constituencies'


    	

