from django.http import HttpResponseNotFound
from django.shortcuts import render
from joblib import load

from .models import Prediction
from .forms import PredictionForm

pipelineLoaded = load('../../model/pipeline.bin')


def index(request):
    if (request.method != 'POST' and request.method != 'GET'):
        return HttpResponseNotFound()

    if (request.method == 'GET'):
        form = PredictionForm()
        return render(request, 'api/index.html', {'form': form})

    form_submitted = PredictionForm(request.POST)
    context = {
        'form': form_submitted
    }
    if (form_submitted.is_valid()):
        new_prediction = Prediction(**form_submitted.cleaned_data)
        new_prediction.predict(pipelineLoaded)
        new_prediction.save()
        context['prediction'] = new_prediction.prediction/10000

    return render(request, 'api/index.html', context)
