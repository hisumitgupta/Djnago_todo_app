from drf.views import *
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('taskapi/',taskapi.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
