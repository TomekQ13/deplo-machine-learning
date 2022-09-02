from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from joblib import load
from .models import Prediction
from django.http import HttpResponseNotFound, HttpResponseBadRequest

pipelineLoaded = load('../../model/pipeline.bin')


@csrf_exempt
def index(request):

    if (request.method != 'POST'):
        return HttpResponseNotFound()

    required_attributes = {
        'age',
        'sex',
        'embarked',
        'pclass',
        'sibsp',
        'parch',
        'fare'
    }

    raw_data = json.loads(request.body)
    prediction_data = {}
    for attribute in required_attributes:
        if attribute not in raw_data:
            return HttpResponseBadRequest(json.dumps({'message': f'{attribute} attribute is missing in the body'}))
        prediction_data[attribute.lower()] = raw_data[attribute]

    new_prediction = Prediction(**prediction_data)
    new_prediction.predict(pipelineLoaded)
    new_prediction.save()
    return JsonResponse({'survived_probability': new_prediction.prediction})
