from django.http import JsonResponse


def index(request):
    print(request.POST)
    return JsonResponse({'message': 'Hello'})
