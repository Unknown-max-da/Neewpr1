from django.urls import path
from .views import personn, personn_detail

urlpatterns=[
    path('person/', personn,name='people'),
    path('persons/<int:id>/', personn_detail, name='personn_detail')
]