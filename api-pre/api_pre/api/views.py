from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from joblib import load
from .models import Prediction
from django.http import HttpResponseNotFound

pipelineLoaded = load('../../model/pipeline.bin')


@csrf_exempt
def index(request):

    if (request.method != 'POST'):
        return HttpResponseNotFound()

    a = json.loads(request.body)
    new = Prediction(**a, prediction=-1)
    new.save()
    new.predict(pipelineLoaded)
    new.save()
    # print(pipelineLoaded)
    return JsonResponse({'message': 'Hello'})
