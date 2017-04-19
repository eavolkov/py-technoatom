from django.http import HttpResponse


def sample_view(request, value):
    try:
        value = int(value)
    except ValueError:
        return HttpResponse('Fail', status=400)
    return HttpResponse('OK')

