from django.urls import path
from . import views

urlpatterns = [
    path('', views.consignment_form, name='consignment_form'),
]
