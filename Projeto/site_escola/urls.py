from django.urls import path

from site_escola.views import home, melhorias, portifolio

urlpatterns = [
    path('', home),  # Home
    path('melhorias', melhorias),
    path('Equipe', portifolio),
    
]