from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from joblib import load
from .models import Prediction

#pipelineLoaded = load('../../model/pipeline.bin')


@csrf_exempt
def index(request):
    a = json.loads(request.body)
    new = Prediction(**a, prediction=-1)
    new.save()
    new.predict()
    # print(pipelineLoaded)
    return JsonResponse({'message': 'Hello'})
