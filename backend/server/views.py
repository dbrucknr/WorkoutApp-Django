from django.http import JsonResponse


def data_test(request):
    data = {
        "data": "packet"
        }
    return JsonResponse(data)