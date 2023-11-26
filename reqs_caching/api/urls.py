from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import VisaReqsView, MasterReqsView


app_name = 'api_casher'
urlpatterns = [
    path('visa/', VisaReqsView.as_view()),
    re_path(r'master/(?P<order_id>[a-zA-Z0-9-]+)', MasterReqsView.as_view()),
]
