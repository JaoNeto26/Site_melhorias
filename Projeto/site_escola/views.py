from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'site_escola/pages/site.html')


def melhorias(request):
    return HttpResponse('site_escola/pages/pagina_melhoria.html')
 

def portifolio(request):
    return HttpResponse('site_escola/pages/portifolio.html')
