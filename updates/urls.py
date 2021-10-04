from django.urls import path

from updates.views import json_example_view, JsonCVB, SerializedJsonDetailView

app_name = 'api'

urlpatterns = [
    path('json/', json_example_view),
    path('json1/', JsonCVB.as_view()),
    path('json2/', SerializedJsonDetailView.as_view())
]
