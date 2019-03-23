import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties, Constituencies

counties_mapping = {
    'objectid' : 'OBJECTID',
    'id_field' : 'ID_',
    'county_nam' : 'COUNTY_NAM',
    'const_code' : 'CONST_CODE',
    'constituen' : 'CONSTITUEN',
    'county_cod' : 'COUNTY_COD',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

county_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/counties/counties.shp'))

def load_counties_shapefile(verbose=True):
	lm = LayerMapping(Counties, county_shp, counties_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)



constituencies_mapping = {
    'objectid' : 'OBJECTID',
    'county_nam' : 'COUNTY_NAM',
    'const_code' : 'CONST_CODE',
    'constituen' : 'CONSTITUEN',
    'county_ass' : 'COUNTY_ASS',
    'county_a_1' : 'COUNTY_A_1',
    'regist_cen' : 'REGIST_CEN',
    'registrati' : 'REGISTRATI',
    'county_cod' : 'COUNTY_COD',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

constituency_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/constituencies/constituencies.shp'))

def load_constituencies_shapefile(verbose=True):
	lm = LayerMapping(Constituencies, constituency_shp, constituencies_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)