from django.urls import path

from site_escola.views import home

urlpatterns = [
    path('', home),  # Home
    
]