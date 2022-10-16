from django.urls import path
from .views import test_view


urlpatterns = [
    path('ws/', test_view, name='echo'),
    ]