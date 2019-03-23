from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from typing import Any

from .models import Counties, Incidences, Constituencies
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# ml stuff
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

my_imputer = SimpleImputer()
from pmdarima.arima import auto_arima
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'views/home.html'


def county_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')


def constituency_datasets(request):
    constituencies = serialize('geojson', Constituencies.objects.all())
    return HttpResponse(constituencies, content_type='json')


def point_datasets(request):
    points = serialize('geojson', Incidences.objects.all())
    return HttpResponse(points, content_type='json')


class PopulationPageView(TemplateView):
    template_name = 'views/population.html'


class WastageRatePageView(TemplateView):
    template_name = 'views/wastage_rate.html'


class EPIDosagePageView(TemplateView):
    template_name = 'views/epi_dosage.html'


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        df = pd.read_csv(uploaded_file_url[1:])
        data = df

        # preprocessing (since arima takes univariate series as input)
        data.drop(['periodid', 'periodname', 'periodcode', 'perioddescription', 'Total BCG doses stocked',
                   'Total BCG doses used', 'Total BCG doses wasted'], axis=1, inplace=True)
        data = data.interpolate(limit_direction='both')

        # divide into train and validation set
        train = data[14:37]
        valid = data[25:32]

        # plotting the data
        train["BCG Wastage Rate"].plot()
        plt.savefig('train.png')
        valid["BCG Wastage Rate"].plot()
        plt.savefig('static/plots/wastage_rate/validation.png')

        data = data[['BCG Wastage Rate']].replace(np.NaN, 0)
        data = data.fillna(method='pad')
		
        #building the model
        model = auto_arima(train, trace=True,m=12, error_action='ignore', suppress_warnings=True)
        model.fit(train)

        forecast = model.predict(n_periods=len(valid))
        forecast = pd.DataFrame(forecast,index = valid.index,columns=['Prediction'])

        #plot the predictions for validation set
        plt.plot(train, label='Train')
        plt.plot(valid, label='Valid')
        plt.plot(forecast, label='Prediction')
        plt.legend(['Train', 'Valid', 'Prediction'], loc=2)
        #plt.show()

        plt.savefig('static/plots/wastage_rate/forecast.png')

        #calculate rmse
        rms = sqrt(mean_squared_error(valid,forecast))
        return render(request, 'views/wastage_rate.html', {
            'uploaded_file_url': uploaded_file_url,
            'show_dataset': True,
			'show_forecast': True,
            'rmse':rms
        })
    return render(request, 'views/wastage_rate.html')
