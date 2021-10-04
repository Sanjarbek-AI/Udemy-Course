import json

from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from updates.models import UpdateModel


def json_example_view(request):
    data = {
        "count": 1000,
        "context": "Good Day Everybody !"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCVB(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "context": "Good Day Everybody !"
        }
        return JsonResponse(data)


class SerializedJsonDetailView(View):
    def get(self, request, *args, **kwargs):
        data = UpdateModel.objects.all().serialize()
        return HttpResponse(data, content_type='application/data')
